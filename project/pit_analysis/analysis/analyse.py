import numpy as np
from functools import partial

pit_percent = 0.17
working_percent = 1
commune_pit_participation = 0.3934
district_pit_participation = 0.1025
province_pit_participation = 0.016


def is_commune(row):
    return "name" in row.index and len(row.name) == 7


def is_province(row):
    return "superior" not in row.index


def get_key(key, population_data):
    if key in population_data.index:
        return key
    assert (key[-1] == "3" or key[-1] == "2")
    if key[-1] == "3":
        new_end_char = "2"
    else:
        new_end_char = "3"
    return key[: -1] + new_end_char


def calc_pit_population(population_data, row):
    return population_data.at[get_key(row.name, population_data), "population"] * working_percent


def calc_total_civilians_income(row):
    if is_province(row):
        multiplication_factor = province_pit_participation
    elif is_commune(row):
        multiplication_factor = commune_pit_participation
    else:
        multiplication_factor = district_pit_participation
    return row["pit_value"] / pit_percent / multiplication_factor


def calc_civilians_income(row):
    return row["total_civilians_income"] / row["pit_population"]


def get_subject_units(data, row):
    name = row["name"] if "name" in row.index else row.name
    return data[data["superior"] == name]


def calc_subject_units_income_variance(data, row):
    subject_units_data = get_subject_units(data, row)
    if subject_units_data.empty:
        return np.nan
    return subject_units_data["civilians_income"].var()


def calc_income_based_on_subject_units(data, row):
    subject_units_data = get_subject_units(data, row)
    if subject_units_data.empty:
        return np.nan
    return np.sum(subject_units_data["total_civilians_income"]) / np.sum(subject_units_data["pit_population"])


def add_columns(data, new_column_formulas):
    for key in new_column_formulas:
        data[key] = data.apply(new_column_formulas[key], axis=1)


def analyse_units_locally(data, population_data):
    add_columns(data,
                {"pit_population": partial(calc_pit_population, population_data),
                 "total_civilians_income": calc_total_civilians_income,
                 "civilians_income": calc_civilians_income})


def analyse_subject_units(data, subject_data):
    add_columns(data,
                {"subject_units_civilians_income_variance": partial(calc_subject_units_income_variance, subject_data),
                 "civilians_income_based_on_subject_units": partial(calc_income_based_on_subject_units, subject_data)})
