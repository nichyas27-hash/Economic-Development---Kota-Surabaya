import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

data = pd.DataFrame({
    "lat": [-7.2575],
    "lon": [112.7521],
    "kota": ["Surabaya"]
})

fig = px.scatter_mapbox(
    data,
    lat="lat",
    lon="lon",
    hover_name="kota",
    zoom=10
)

fig.update_layout(
    mapbox_style="open-street-map"
)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run(debug=True)