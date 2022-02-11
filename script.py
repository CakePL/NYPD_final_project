#importuje tylko pojedyncze funkcje, zeby podkreslic ze to one stanowia interfejs biblioteki
#a pozostale - implementacje
import argparse
from pit_analysis.io.load import load_pit_commune_data, load_pit_district_data, load_pit_province_data, \
    load_population_data, load_population_province_data
from pit_analysis.analysis.analyse import analyse_units_locally, analyse_subject_units
from pit_analysis.analysis.compare import split_districts_to_districts_and_citieswdr, connect_old_and_new_data
from pit_analysis.io.visualize import show_commune_interactive_chart, show_citywdr_interactive_chart, \
    show_district_interactive_chart, show_province_interactive_chart

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    arg_names = ("--pit_citywdr_2019", "--pit_citywdr_2020",
                 "--pit_commune_2019", "--pit_commune_2020",
                 "--pit_district_2019", "--pit_district_2020",
                 "--pit_province_2019", "--pit_province_2020",
                 "--population_commune_2019", "--population_commune_2020",
                 "--population_district_2019", "--population_district_2020",
                 "--population_province_2019", "--population_province_2020")
    for arg_name in arg_names:
        parser.add_argument(arg_name, type=str, metavar="PATH", required=True)
    args = parser.parse_args()

    commune_2019_data = load_pit_commune_data(args.pit_commune_2019)
    commune_2020_data = load_pit_commune_data(args.pit_commune_2020)
    district_2019_data = load_pit_district_data([args.pit_district_2019, args.pit_citywdr_2019])
    district_2020_data = load_pit_district_data([args.pit_district_2020, args.pit_citywdr_2020])
    province_2019_data = load_pit_province_data(args.pit_province_2019)
    province_2020_data = load_pit_province_data(args.pit_province_2020)

    commune_2019_population = load_population_data(args.population_commune_2019)
    commune_2020_population = load_population_data(args.population_commune_2020)
    district_2019_population = load_population_data(args.population_district_2019)
    district_2020_population = load_population_data(args.population_district_2020)
    province_2019_population = load_population_province_data(args.population_province_2019)
    province_2020_population = load_population_province_data(args.population_province_2020)

    analyse_units_locally(commune_2019_data, commune_2019_population)
    analyse_units_locally(commune_2020_data, commune_2020_population)
    analyse_units_locally(province_2019_data, province_2019_population)
    analyse_units_locally(province_2020_data, province_2020_population)
    analyse_units_locally(district_2019_data, district_2019_population)
    analyse_units_locally(district_2020_data, district_2020_population)

    analyse_subject_units(district_2019_data, commune_2019_data)
    analyse_subject_units(district_2020_data, commune_2020_data)
    analyse_subject_units(province_2019_data, district_2019_data)
    analyse_subject_units(province_2020_data, district_2020_data)

    district_2019_result, citywdr_2019_result = split_districts_to_districts_and_citieswdr(district_2019_data)
    district_2020_result, citywdr_2020_result = split_districts_to_districts_and_citieswdr(district_2020_data)

    citywdr_final_result = connect_old_and_new_data(citywdr_2020_result, citywdr_2019_result)
    commune_final_result = connect_old_and_new_data(commune_2020_data, commune_2019_data)
    district_final_result = connect_old_and_new_data(district_2020_result, district_2019_result)
    province_final_result = connect_old_and_new_data(province_2020_data, province_2019_data)

    show_citywdr_interactive_chart(citywdr_final_result)
    show_commune_interactive_chart(commune_final_result)
    show_district_interactive_chart(district_final_result)
    show_province_interactive_chart(province_final_result)
