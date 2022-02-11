import pandas as pd
import numpy as np
import enum
from functools import partial

normalized_names = {"karkonoski (jeleniogórski)": "jeleniogórski",
                    "wągrowiecki": "wągrowicki"}

normalized_codes = {"0224032": "0224033",
                    "0602062": "0602063",
                    "0608052": "0608053",
                    "1004062": "1004063",
                    "1018042": "1018043",
                    "1210022": "1210023",
                    "1409062": "1409063",
                    "1420042": "1420043",
                    "1420112": "1420113",
                    "1438052": "1438053",
                    "1813022": "1813023",
                    "2602092": "2602093",
                    "2609032": "2609033",
                    "3001022": "3001023",
                    "3007052": "3007053"}


class Jst(enum.Enum):
    COMMUNE = enum.auto()
    DISTRICT = enum.auto()
    PROVINCE = enum.auto()


def set_column(data, column_name, column_formula):
    data[column_name] = data.apply(column_formula, axis=1)


def normalize(pit_data):
    if "name" in pit_data.columns:
        set_column(pit_data, "name", lambda row: normalized_names.get(row["name"], row["name"]))
    pit_data.index = pit_data.apply(lambda row: normalized_codes.get(row.name, row.name), axis=1)


def cacl_total_unit_income(data, row):
    return np.sum(data[row.name:row.name]["pit_value"])


def calc_pit_value(data, row):
    return data[row.name:row.name]["pit_value"][-1]


def establish_total_unit_income(data):
    set_column(data, "total_unit_income", partial(cacl_total_unit_income, data))
    set_column(data, "pit_value", partial(calc_pit_value, data))
    data.drop_duplicates(inplace=True)


def load_pit_data(jst, file_path):
    df = pd.read_excel(file_path, dtype=str, usecols=list(range(7)) + [10],
                       skiprows=list(range(3)) + list(range(4, 7)))
    result = pd.DataFrame({"code": df["WK"], "name": df["Nazwa JST"], "pit_value": df.iloc[:, 7]})
    if jst != Jst.PROVINCE:
        result["code"] += df["PK"]
    if jst == Jst.COMMUNE:
        result["code"] += df["GK"]
        result["code"] += df["GT"]
    if jst == Jst.PROVINCE:
        result.set_index("name", inplace=True)
    else:
        if jst == Jst.DISTRICT:
            result["superior"] = df["województwo"]
        else:
            result["superior"] = df["powiat"]
        result.set_index("code", inplace=True)
    normalize(result)
    result = result.astype({"pit_value": float}, copy=False)
    establish_total_unit_income(result)
    return result


def load_pit_commune_data(file_path):
    return load_pit_data(Jst.COMMUNE, file_path)


def load_pit_district_data(file_paths):
    return pd.concat([load_pit_data(Jst.DISTRICT, file_path) for file_path in file_paths])


def load_pit_province_data(file_path):
    return load_pit_data(Jst.PROVINCE, file_path)


def load_population_province_data(file_path):
    result = pd.read_excel(file_path, usecols=range(2), skiprows=range(8), nrows=16,
                           names=["name", "population"], header=None)
    result["name"] = result["name"].str.lower()
    result.set_index("name", inplace=True)
    return result


def load_population_data(file_path):
    result = pd.read_excel(file_path, usecols=range(1, 3), skiprows=range(9), names=["code", "population"],
                           header=None, dtype=str).dropna()
    result.set_index("code", inplace=True)
    result.index = result.index.astype(str)
    return result.astype({"population": float}, copy=False)
