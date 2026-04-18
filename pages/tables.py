from dash import html
import dash_bootstrap_components as dbc
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.table.inflasi import Inflasi
from components.table.sdgs import SDGs
import dash

dash.register_page(__name__, path="/tables")

layout = dbc.Container([
    dbc.Row([
        html.H3(["Data Ekonomi - Kota Surabaya"], className="mb-4"),
        html.P(["""Data yang digunakan diperoleh dari kerja sama antar Dinas Tenaga Kerja (Disnaker) Kota Surabaya, dan publikasi Badan Pusat Statistik (BPS) Kota Surabaya.
                Terkait data inflasi yang meliputi inflasi bulanan (month-to-month), tahunan (year-on-year), dan kumulatif bersumber langsung dari Badan Pusat Statistik Kota Surabaya."""], style={"textAlign":"justify"}),
        html.Span([
            dbc.Badge("Table", color="success", className="me-1"),
            dbc.Badge("Data", color="warning", className="me-1"),
            dbc.Badge("Disnaker", color="dark", className="me-1", href="https://disnaker.surabaya.go.id/"),
            dbc.Badge("BPS", color="dark", className="me-1", href="https://surabayakota.bps.go.id/")
        ]),
    ], className="mb-4"),
    dbc.Row([
        dbc.Tabs([
            dbc.Tab(
                label="Indikator SDGs-8",
                children=[
                    SDGs, 
                    html.Span([
                        dbc.Badge("SDGs-8", color="success", className="me-1"),
                        dbc.Badge("Economic", color="warning", className="me-1")
                    ])
                ]
            ),
            dbc.Tab(
                label="Data Inflasi",
                children=[
                    Inflasi,
                    html.Span([
                        dbc.Badge("Inflasi", color="success", className="me-1"),
                        dbc.Badge("Economic", color="warning", className="me-1")
                    ])
                ]
            )
        ])
    ])
], style={"maxWidth":"80%", "marginLeft":"20%", "marginTop":"1%"})