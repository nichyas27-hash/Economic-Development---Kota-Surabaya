import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.figure.overview import TPT, pertumbuhanEkonomi, pdrb, umkm
from components.card.cd import cardImage
from callbacks import overview
dash.register_page(__name__, path="/overview")

layout = dbc.Container([
    dbc.Row([
        html.H3(["Economic Growth - Kota Surabaya"], className="mb-4")]),
    dbc.Row([
        dbc.Col([
            html.P(["""Berdasarkan data SDGs 8 Kota Surabaya tahun 2015–2025, kondisi ekonomi menunjukkan tren pemulihan dan peningkatan setelah terdampak pandemi pada tahun 2020. 
                Tingkat pengangguran yang sempat meningkat pada masa pandemi kemudian menurun secara bertahap, sementara pertumbuhan ekonomi kembali stabil pada kisaran 5–6%. 
                Selain itu, jumlah UMKM terus meningkat signifikan, yang menunjukkan semakin berkembangnya aktivitas ekonomi dan kewirausahaan di Kota Surabaya. 
                Secara umum, hal ini mencerminkan pemulihan ekonomi dan meningkatnya peluang kerja di Surabaya."""], style={"textAlign":"justify"}),
        ], width=10),
        dbc.Col([
            html.Div([
            cardImage(Src="assets/icons/8.png")               
            ], id="indicator_cards", n_clicks=0, className="info-card", style={'cursor':"pointer"}),
        ], width=2),
    ]),
    dbc.Row([
        html.Span([
            dbc.Badge("SDGs-8", color="success", className="me-1"),
            dbc.Badge("Ekonomi", color="warning", className="me-1"),
            dbc.Badge("Kota Surabaya", color="dark", className="me-1"),
            dbc.Badge("2025", color="secondary", className="me-1")
        ])       
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5("Pertumbuhan Ekonomi")),
                dbc.CardBody([
                    dcc.Graph(figure=pertumbuhanEkonomi),
                    dbc.Badge("Economic Groth", color="warning", className="me-1")
                    ])
                ])
            ]),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5("Gross Domestik Produk")),
                dbc.CardBody([
                    dcc.Graph(figure=pdrb),
                    html.Span([
                        dbc.Badge("GDP", color="success", className="me-1"),
                        dbc.Badge("PDRB", color="warning", className="me-1")])
                    ])
                ])
            ]),            
        ]),
    dbc.Row([
        dbc.Card([
            dbc.CardHeader(html.H5("Tingkat Pengangguran")),
            dbc.CardBody([
                dcc.Graph(figure=TPT),
                dbc.Badge("Unemployment", color="warning", className="me-1")
            ])
        ])
    ]),
    dbc.Row([
        dbc.Card([
            dbc.CardHeader(html.H5("Jumlah UMKM")),
            dbc.CardBody([
                dcc.Graph(figure=umkm),
                html.Span([
                    dbc.Badge("Mikro Economic", color="success", className="me-1"),
                    dbc.Badge("UMKM", color="warning", className="me-1")
                ])
            ])
        ])
    ]),
    dbc.Modal(
        [
        dbc.ModalHeader(dbc.ModalTitle("Detail SDG")),
        dbc.ModalBody(id="modal-content"),
        ],
        id="info_card",
        is_open=False
    )
], style={"maxWidth":"80%", "marginLeft":"20%", "marginTop":"1%"})

