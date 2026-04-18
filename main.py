import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import page_container
from callbacks.main import search

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
    pages_folder="./pages",
    use_pages=True,
    suppress_callback_exceptions=True
)

sidebar = html.Div(
    [
        html.Div([
            html.Img(src="assets/icons/Logo.png", width="100%", 
                     className="logo"),
        ], className="p-3"),

        html.Hr(),

        dbc.Nav(
            [
                dbc.NavLink([html.I(className="fas fa-pie-chart me-2"), "Overview"],
                            href="/overview", active="exact"),
                dbc.NavLink([html.I(className="fas fa-line-chart me-2"), "Inflation"],
                            href="/inflation", active="exact"),
                dbc.NavLink([html.I(className="fas fa-table me-2"), "Data Tables"],
                            href="/tables", active="exact"),
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
        "display":"block"
    },
)

topbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("Economic Development", className="text-white"),

            dbc.Input(type="search", placeholder="Cari di Google...",
                      style={"width": "300px"}, id="search-box"),
            dcc.Location(id="redirect"),
            dbc.Nav([
                dbc.NavItem(dbc.NavLink(html.I(className="fas fa-home"), href="/")),
                dbc.NavItem(dbc.NavLink(html.I(className="fas fa-user-circle fa-lg"), href="https://nichyas27.site/")),
            ]),
        ], fluid=True
    ),
    color="dark",
    dark=True,
    style={
        "margin-left": "20%","display":"block"
    }
)

app.layout = html.Div([
    sidebar,
    topbar,
    page_container
], style={"maxWidth":"100%", "width":"100%"})

if __name__ == "__main__":
    app.run(debug=True)