import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from datetime import datetime as dt
from dash_app.src.gas_oil_chart import EnergyPriceChart
from dash_app.src.gas_oil_data import EnergyPriceData
from dash_app.src.gas_oil_chart import EnergyBarChart


# Prepare the data set
data = EnergyPriceData()
type = "gas"
data.process_data_for_type(type)
Date = "2009-03-05"
data.process_data_for_date(Date)

# Create the figures
lc = EnergyPriceChart(data)
fig_lc = lc.create_chart(type)
all_line_chart = lc.draw_all_line_chart()
bar_chart = EnergyBarChart(data)
fig_bc = bar_chart.create_chart(Date)


def create_dash_app(flask_app):
    # create the Dash app object
    app = dash.Dash(
        external_stylesheets=[dbc.themes.LUX],
        server=flask_app,
        url_base_pathname='/dashboard/',
        meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    )

    # create the app layout using Bootstrap containers and rows
    app.layout = dbc.Container(
        fluid=True,
        children=[
            html.Br(),
            html.H1("Oil and Gas price"),
            html.P(
                "Dash app that can provide charts for analysing trend, pattern, and correlations of oil and gas price.",
                className="lead",
            ),
            dbc.Row(
                dbc.Col(
                    children=[
                        html.H2("1. Line chart"),
                        html.P("Select an energy source you want to display on chart", className="lead",),
                    ]
                )
            ),
            dbc.Row(
                [
                    # First column
                    dbc.Col(
                        width=3,
                        children=[
                            html.H4("Select energy type(brent and wti are oil prices)"),
                            dcc.Dropdown(
                                id="type-select",
                                options=[{"label": x, "value": x} for x in data.type_list],
                                value="gas",
                            ),
                            html.Br(),
                        ],
                    ),
                    # Second column for the figure
                    dbc.Col(
                        width=9,
                        children=[html.H2("oil and gas price"), dcc.Graph(id="line-chart", figure=fig_lc)],
                    ),
                ]
            ),
            dbc.Row(
                dbc.Col(
                    width=9,
                    align="center",
                    children=[
                        html.H3("all the energy source on same chart for comparison"),
                        dcc.Graph(id="all-line-chart", figure=all_line_chart),
                    ],
                ),
            ),
            dbc.Row(
                [
                    # First column
                    dbc.Col(
                        children=[
                            html.H1("2. Bar chart"),
                            dcc.DatePickerSingle(id="my-date-picker-single", date=dt(2009, 1, 13), display_format="YYYY-MM-DD",),
                        ],
                    ),
                    # Second column for the bar chart figure
                    dbc.Col(
                        width=9,
                        children=[html.H2("daily price of oil and gas"), dcc.Graph(id="bar-chart", figure=fig_bc),],
                    ),
                ]
            ),
        ],
    )

    # define the callback function for updating the line chart
    @app.callback(Output("line-chart", "figure"), Input("type-select", "value"))
    def update_line_chart(type_select):
        data.process_data_for_type(type_select)
        fig_lc = lc.create_chart(type_select)
        return fig_lc

    # define the callback function for updating the bar chart
    @app.callback(Output("bar-chart", "figure"), Input("my-date-picker-single", "date"))
    def update_bar_chart(date_select):
        data.process_data_for_date(date_select)
        fig_bc = bar_chart.create_chart(date_select)
        return fig_bc

    return flask_app
