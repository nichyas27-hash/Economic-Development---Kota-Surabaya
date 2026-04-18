from dash import html
import dash_bootstrap_components as dbc

def cardImage(Src):
    return dbc.Card([
        dbc.CardImg(src=Src)
    ])