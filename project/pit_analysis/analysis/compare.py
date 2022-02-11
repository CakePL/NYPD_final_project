def connect_old_and_new_data(new_data, old_data):
    result = new_data.merge(old_data, how="left", left_index=True, right_index=True, suffixes=("_2020", "_2019"),
                            validate="1:1")
    if "name_2020" in result.columns:
        result["name_2020"] = result.apply(lambda row: row["name_2020"] + " " + row.name, axis=1)
        result.set_index("name_2020", inplace=True)

    for column in result.columns:
        if column not in (
                "total_unit_income_2020", "total_unit_income_2019",
                "civilians_income_2020", "civilians_income_2019",
                "subject_units_civilians_income_variance_2020",
                "subject_units_civilians_income_variance_2019",
                "civilians_income_based_on_subject_units_2020",
                "civilians_income_based_on_subject_units_2019"
        ):
            result.drop(column, axis=1, inplace=True)

    return result


def split_districts_to_districts_and_citieswdr(data):
    citywdr_indexes = data.isnull().any(axis=1)
    result_citywdr = data[citywdr_indexes].copy()
    result_district = data[~citywdr_indexes].copy()

    for column in ("civilians_income_based_on_subject_units", "subject_units_civilians_income_variance"):
        result_citywdr.drop(column, axis=1, inplace=True)

    return result_district, result_citywdr
