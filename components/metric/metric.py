from dash import html
import dash_bootstrap_components as dbc

def createMetric(title, value, icon, color):
    return dbc.Card([
        dbc.CardHeader(title),
        dbc.CardBody([
            html.I(className=icon),
            html.Span(value)
        ], className=color)
    ])