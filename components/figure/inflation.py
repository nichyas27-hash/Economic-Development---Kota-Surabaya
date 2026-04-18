from components.figure.fig import lineChart
import pandas as pd

mom = pd.read_csv("assets/data/InflationMom.csv")
yoy = pd.read_csv("assets/data/InflationYoy.csv")

bulanan = lineChart(
    Data={'Tahun-Bulan':mom['Tahun-Bulan'], 'Inflasi (%)':mom['Inflasi (%)']},
    X='Tahun-Bulan', Y='Inflasi (%)', Template="plotly_white", Markers=''
)
tahunan = lineChart(
    Data={'Tahun-Bulan':yoy['Tahun-Bulan'], 'Inflasi (%)':yoy['Inflasi (%)']},
    X='Tahun-Bulan', Y='Inflasi (%)', Template="plotly_white", Markers=''
)