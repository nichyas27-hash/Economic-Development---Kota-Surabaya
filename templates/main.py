import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import page_container

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
)

sidebar = html.Div(
    [
        html.Div([
            html.Img(src="assets/icons/Logo.png", width="20%", 
                     className="logo"),
        ], className="p-3"),

        html.Hr(),

        dbc.Nav(
            [
                dbc.NavLink([html.I(className="fas fa-chart-line me-2"), "Overview"],
                            href="#", active="exact"),
                dbc.NavLink([html.I(className="fas fa-pie-chart me-2"), "Data Visualization"],
                            href="#", active="exact"),
                dbc.NavLink([html.I(className="fas fa-table me-2"), "Data Tables"],
                            href="#", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "20%",
        "padding": "10px",
        "backgroundColor": "#1f2937",
        "color": "white",
    },
)

topbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("Economic Development", className="text-white"),

            dbc.Input(type="search", placeholder="Search...",
                      style={"width": "300px"}),

            dbc.Nav([
                dbc.NavItem(dbc.NavLink(html.I(className="fas fa-bell"))),
                dbc.NavItem(dbc.NavLink(html.I(className="fas fa-user-circle fa-lg"))),
            ]),
        ], fluid=True
    ),
    color="dark",
    dark=True,
    style={
        "margin-left": "20%",
    }
)

app.layout = html.Div([
    sidebar,
    topbar,
], style={"maxWidth":"100%"})

if __name__ == "__main__":
    app.run(debug=True)