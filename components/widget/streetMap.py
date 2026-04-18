import dash
from dash import html
import folium

map = folium.Map(location=[-7.2575,112.7521], zoom_start=13)
map.save("map.html")

def app():
    map = html.Iframe(
    srcDoc=open("map.html","r").read(),
    width="100%",
    height="300px"
    )
    return map
