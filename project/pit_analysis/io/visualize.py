import pandas as pd

pd.options.plotting.backend = "plotly"

label_dict = {"total_unit_income_2019": "profit in 2019",
              "total_unit_income_2020": "profit in 2020",
              "civilians_income_2019": "earning based on pit tax in 2019",
              "civilians_income_2020": "earning based on pit tax in 2020",
              "subject_units_civilians_income_variance_2019": "variance in 2019",
              "subject_units_civilians_income_variance_2020": "variance in 2020",
              "civilians_income_based_on_subject_units_2019": "earning based on pit tax in subject units in 2019",
              "civilians_income_based_on_subject_units_2020": "earning based on pit tax in subject units in 2020"}


def update_one_label(fig_trace):
    return fig_trace.update(name=label_dict[fig_trace.name],
                            legendgroup=label_dict[fig_trace.name],
                            hovertemplate=fig_trace.hovertemplate.replace(fig_trace.name, label_dict[fig_trace.name]))


def update_labels(fig):
    fig.for_each_trace(update_one_label)


def show_chart(data, name, columns, title):
    data.index.rename(name, inplace=True)
    fig = data.plot.bar(y=columns, barmode="group", title=title)
    update_labels(fig)
    fig.show()


def show_citywdr_interactive_chart(data):
    name = "city with district rights (with code)"
    show_chart(data,
               name,
               ["total_unit_income_2019", "total_unit_income_2020"],
               "total profits of cities with district rights from pit tax in 2019 and 2020")
    show_chart(data,
               name,
               ["civilians_income_2019", "civilians_income_2020"],
               "average earnings of citizens of cities with district rights calculated on the basis of pit tax"
               + " in 2019 and 2020")


def show_commune_interactive_chart(data):
    name = "commune (with code)"
    show_chart(data,
               name,
               ["total_unit_income_2019", "total_unit_income_2020"],
               "total profits of communes from pit tax in 2019 and 2020")
    show_chart(data,
               name,
               ["civilians_income_2019", "civilians_income_2020"],
               "average earnings of citizens of communes calculated on the basis of pit tax in 2019 and 2020")


def show_district_interactive_chart(data):
    name = "district (with code)"
    show_chart(data,
               name,
               ["total_unit_income_2019", "total_unit_income_2020"],
               "total profits of districts from pit tax in 2019 and 2020")
    show_chart(data,
               name,
               ["subject_units_civilians_income_variance_2019", "subject_units_civilians_income_variance_2020"],
               "variances of average earnings (on the basis of pit tax) in subject communes in 2019 and 2020")
    show_chart(data,
               name,
               ["civilians_income_2019", "civilians_income_based_on_subject_units_2019",
                "civilians_income_2020", "civilians_income_based_on_subject_units_2020"],
               "average earnings of citizens of districts, calculated on the basis of pit tax"
               + " and on the basis of pit tax in subject communes - comparison")


def show_province_interactive_chart(data):
    name = "province"
    show_chart(data,
               name,
               ["total_unit_income_2019", "total_unit_income_2020"],
               "total profits of provinces from pit tax in 2019 and 2020")
    show_chart(data,
               name,
               ["subject_units_civilians_income_variance_2019", "subject_units_civilians_income_variance_2020"],
               "variances of average earnings (on the basis of pit tax) in subject districts"
               + " and cities with district rights in 2019 and 2020")
    show_chart(data,
               name,
               ["civilians_income_2019", "civilians_income_based_on_subject_units_2019",
                "civilians_income_2020", "civilians_income_based_on_subject_units_2020"],
               "average earnings of citizens of provinces, calculated on the basis of pit tax"
               + " and on the basis of pit tax in subject units - comparison")
