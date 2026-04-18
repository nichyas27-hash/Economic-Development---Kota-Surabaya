import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.figure.inflation import bulanan, tahunan

dash.register_page(__name__, path="/inflation")

layout = dbc.Container([
    dbc.Row([
        html.H3(["Inflation - Kota Surabaya"], className="mb-4"),
        html.P(["""Pada tahun 2025, inflasi di Surabaya tercatat sekitar 2,96% (year-on-year) dan masih berada dalam kisaran target inflasi nasional, 
               sehingga mencerminkan kondisi harga yang relatif stabil. Sepanjang tahun terjadi beberapa periode inflasi dan deflasi, 
               dengan kenaikan harga terutama dipengaruhi oleh komoditas pangan seperti beras, cabai, dan daging ayam serta peningkatan permintaan saat periode Ramadan–Idul Fitri."""], style={"textAlign":"justify"}),
        html.Span([
            dbc.Badge("Inflasi", color="warning", className="me-1"),
            dbc.Badge("Kota Surabaya", color="dark", className="me-1"),
            dbc.Badge("2025", color="secondary", className="me-1")
        ])
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H6("Inflasi M-o-M per Desember 2025")),
                dbc.CardBody([
                    html.I(className="fas fa-arrow-up"),
                    html.Span(" 0,80%")
                ], style={"fontSize":"40px", "fontWeight":"500px"}, className="text-danger")
            ])
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H6("Inflasi Y-o-Y per Desember 2025")),
                dbc.CardBody([
                    html.I(className="fas fa-arrow-up"),
                    html.Span(" 2,96%")
                ], style={"fontSize":"40px", "fontWeight":"500px"}, className="text-danger")
            ])
        ], width=4)
    ], className="mb-4"),
    dbc.Row([
        dcc.Tabs([
            dcc.Tab(
                label="Inflasi M-o-M",
                children=[
                    dcc.Graph(figure=bulanan),
                    html.Span([
                        dbc.Badge("Inflasi Bulanan", color="success", className="me-1"),
                        dbc.Badge("Month to Month", color="warning", className="me-1")
                    ])
                ]    
            ),
            dcc.Tab(
                label="Inflasi Y-o-Y",
                children=[
                    dcc.Graph(figure=tahunan),
                    html.Span([
                        dbc.Badge("Inflasi Tahunan", color="success", className="me-1"),
                        dbc.Badge("Year on Year", color="warning", className="me-1")
                    ])
                ]
            )
        ])
    ])
], style={"maxWidth":"80%", "marginLeft":"20%", "marginTop":"1%"})
