import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# ===== APP =====
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
)

# ===== SIDEBAR =====
sidebar = html.Div(
    [
        html.Div([
            html.H4("My Admin", className="text-white")
        ], className="p-3"),

        html.Hr(),

        dbc.Nav(
            [
                dbc.NavLink([html.I(className="fas fa-home me-2"), "Dashboard"],
                            href="#", active="exact"),
                dbc.NavLink([html.I(className="fas fa-chart-line me-2"), "Analytics"],
                            href="#", active="exact"),
                dbc.NavLink([html.I(className="fas fa-table me-2"), "Data Table"],
                            href="#", active="exact"),
                dbc.NavLink([html.I(className="fas fa-cog me-2"), "Settings"],
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
        "width": "260px",
        "padding": "10px",
        "backgroundColor": "#1f2937",
        "color": "white",
    },
)

# ===== TOP NAVBAR =====
topbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("Admin Dashboard", className="text-white"),

            dbc.Input(type="search", placeholder="Search...",
                      style={"width": "300px"}),

            dbc.Nav([
                dbc.NavItem(dbc.NavLink(html.I(className="fas fa-bell"))),
                dbc.NavItem(dbc.NavLink(html.I(className="fas fa-user-circle fa-lg"))),
            ]),
        ]
    ),
    color="dark",
    dark=True,
    style={
        "margin-left": "260px",
    }
)

# ===== CARDS =====
def info_card(title, value, icon, color):
    return dbc.Card(
        dbc.CardBody([
            html.Div([
                html.I(className=f"{icon} fa-2x"),
            ], className="text-" + color),

            html.H4(value, className="mt-2"),
            html.P(title, className="text-muted"),
        ]),
        className="shadow-sm"
    )

cards = dbc.Row([
    dbc.Col(info_card("Users", "1,245", "fas fa-users", "primary"), md=3),
    dbc.Col(info_card("Revenue", "Rp 25M", "fas fa-wallet", "success"), md=3),
    dbc.Col(info_card("Orders", "320", "fas fa-shopping-cart", "warning"), md=3),
    dbc.Col(info_card("Errors", "3", "fas fa-exclamation-triangle", "danger"), md=3),
], className="g-3")

# ===== MAIN CONTENT =====
content = html.Div(
    [
        topbar,

        html.Div(
            [
                html.H2("Dashboard Overview", className="mb-4"),

                cards,

                html.Div(className="mt-4"),

                dbc.Card(
                    dbc.CardBody([
                        html.H5("Chart Area"),
                        html.Div("Tambahkan grafik Plotly di sini")
                    ]),
                    className="shadow-sm"
                )
            ],
            style={
                "margin-left": "260px",
                "padding": "20px"
            }
        )
    ]
)

# ===== LAYOUT =====
app.layout = html.Div([
    sidebar,
    content
])

# ===== RUN =====
if __name__ == "__main__":
    app.run(debug=True)