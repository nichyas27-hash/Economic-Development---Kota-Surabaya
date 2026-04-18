from dash import Dash, html
from dash import dash_table
import pandas as pd

inflasi = pd.DataFrame(pd.read_csv("assets/data/InflationSet.csv"))

Inflasi = dash_table.DataTable(
    data=inflasi.to_dict("records"),
    columns=[{"name":i, "id": i} for i in inflasi.columns],

    sort_action="native",
    filter_action="native",
    style_table={"overflowX":"auto", "maxWidth":"100%"},
    style_cell={"textAlign":"left"},
    )