from dash import Dash, html
from dash import dash_table
import pandas as pd

sdgs = pd.DataFrame(pd.read_csv("assets/data/SDGs-8.csv"))
inflasi = pd.DataFrame(pd.read_csv("assets/data/InflationSet.csv"))

SDGs = dash_table.DataTable(
    data=sdgs.to_dict("records"),
    columns=[{"name": i, "id": i} for i in sdgs.columns],
    sort_action="native",
    filter_action="native",
    style_table={"overFlowX":"auto"},
    style_cell={"textAlign":"left"},
    )