import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.widget.streetMap import app

dash.register_page(
    __name__,
    path="/",   # halaman pertama yang dibuka
    name="Home"
)

layout = dbc.Container([
    dbc.Row([
        html.H2("Welcome to Economic Development Dashboard"),
        html.H4("Dashboard ini menampilkan indikator ekonomi Kota Surabaya."),       
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            html.P(["""Surabaya adalah kota metropolitan terbesar kedua di Indonesia yang dikenal sebagai pusat perdagangan, industri, dan pendidikan di wilayah Jawa Timur. 
                    Kota ini memiliki sejarah penting dalam perjuangan kemerdekaan Indonesia sehingga sering dijuluki sebagai Kota Pahlawan. 
                    Perkembangan infrastruktur dan ekonominya yang pesat menjadikan Surabaya sebagai salah satu motor pertumbuhan ekonomi di kawasan timur Indonesia. 
                    Selain itu, Surabaya juga terus mengembangkan berbagai program pembangunan kota yang berfokus pada keberlanjutan dan kesejahteraan masyarakat.
                    Dengan kombinasi sejarah, modernisasi, dan dinamika ekonomi, Surabaya menjadi kota yang memiliki peran strategis bagi perkembangan Indonesia."""], style={"textAlign":"justify"}),
            html.Span([
                dbc.Badge("SDGs", color="success", className="me-1"),
                dbc.Badge("Ekonomi", color="warning", className="me-1"),
                dbc.Badge("Kota Surabaya", color="dark", className="me-1"),
                dbc.Badge("2025", color="secondary", className="me-1")
            ]) 
        ], width=7),
        dbc.Col([
            dbc.Card([
                app()
            ])
        ], width=5)
    ]), 
], fluid=True, style={"maxWidth":"80%", "marginLeft":"20%", "marginTop":"1%"})
