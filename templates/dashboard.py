import dash
from dash import html, dcc, callback, Output, Input, ctx
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "/assets/css/dashboard.css"])

df = pd.DataFrame({
    "Year": [2017, 2018, 2019, 2020, 2021],
    "Value": [50, 60, 55, 70, 80]
})

line_fig = px.line(df, x="Year", y="Value")
bar_fig = px.bar(df, x="Year", y="Value")
pie_fig = px.pie(names=["Agri", "Industry", "Services"], values=[30, 40, 30])

radar_fig = px.line_polar(
    r=[10, 12, 9, 11, 13],
    theta=["Goal1", "Goal2", "Goal3", "Goal4", "Goal5"],
    line_close=True
)

def metric_card(title):
    return dbc.Card(
        dbc.CardBody([
            html.Div(title, className="card-title"),
            html.H4("###", className="card-value")
        ]),
        className="shadow-sm"
    )

def chart_card(title, fig):
    return dbc.Card(
        dbc.CardBody([
            html.H6(title),
            dcc.Graph(figure=fig, config={"displayModeBar": False})
        ]),
        className="shadow-sm"
    )


sidebar = html.Div(
    [
        html.H4("SDGs Lumajang", className="text-white"),
        html.Hr(),
        html.Label("Select Year", className="text-white"),
        dcc.Dropdown(
            options=[{"label": str(i), "value": i} for i in range(2017, 2023)],
            value=2021
        ),
        html.Hr(),
        html.Div("Overview", className="menu-item"),
        html.Div("Social", className="menu-item"),
        html.Div("Economy", className="menu-item"),
        html.Div("Environment", className="menu-item"),
        html.Div("Kecamatan", className="menu-item"),
    ],
    className="sidebar"
)

content = dbc.Container(fluid=True, children=[

    html.H3("Dashboard SDGs Kabupaten Lumajang", className="mb-4"),

    # === SDGs Overview ===
    dbc.Row([
        dbc.Col(metric_card("Poverty Rate")),
        dbc.Col(metric_card("HDI")),
        dbc.Col(metric_card("Unemployment")),
        dbc.Col(metric_card("Population")),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(chart_card("SDGs Progress", radar_fig), md=6),
        dbc.Col(chart_card("SDGs Score Over Time", line_fig), md=6),
    ], className="mb-4"),

    # === Social Development ===
    html.H5("Social Development"),
    dbc.Row([
        dbc.Col(chart_card("Poverty Trend", line_fig), md=6),
        dbc.Col([
            metric_card("Stunting Rate"),
            metric_card("Life Expectancy"),
            metric_card("School Enrolment"),
        ], md=6)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(chart_card("Access to Clean Water", bar_fig)),
        dbc.Col(chart_card("Sanitation Access", bar_fig)),
    ], className="mb-4"),

    # === Economic + Environment + Kecamatan ===
    dbc.Row([
        # Economic
        dbc.Col([
            html.H5("Economic Development"),
            chart_card("PDRB Growth", line_fig),
            chart_card("Economic Sectors", pie_fig),
        ], md=4),

        # Environment
        dbc.Col([
            html.H5("Environment"),
            chart_card("Forest Area", bar_fig),
            chart_card("Agricultural Land", line_fig),
            chart_card("Disaster Trend", line_fig),
            chart_card("Waste Management", bar_fig),
        ], md=4),

        # Kecamatan
        dbc.Col([
            html.H5("Kecamatan Comparison"),
            dbc.Card(
                dbc.CardBody([
                    html.Label("Top 5 Kecamatan"),
                    dcc.Dropdown(
                        options=[{"label": f"Kecamatan {i}", "value": i} for i in range(1,6)],
                        value=1
                    ),
                    html.Hr(),
                    html.Table([
                        html.Tr([html.Th("Rank"), html.Th("Kecamatan"), html.Th("Poverty")]),
                        html.Tr([html.Td("1"), html.Td("A"), html.Td("46")]),
                        html.Tr([html.Td("2"), html.Td("B"), html.Td("36")]),
                        html.Tr([html.Td("3"), html.Td("C"), html.Td("54")]),
                    ])
                ])
            )
        ], md=4),
    ])

], className="content")

app.layout = html.Div([
    sidebar,
    content
])

if __name__ == "__main__":
    app.run(debug=True)