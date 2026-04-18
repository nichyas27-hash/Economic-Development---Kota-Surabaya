from components.figure.fig import lineChart, barChart
import pandas as pd

df = pd.read_csv('assets/data/SDGs-8.csv')
TPT = lineChart(
    Data={'Tahun':df['Tahun'], 'TPT (%)':df['TPT (%)']},
    X='Tahun', Y='TPT (%)', Markers='o', Template="seaborn"
)
pertumbuhanEkonomi = lineChart(
    Data={'Tahun':df['Tahun'], 'Pertumbuhan Ekonomi (%)':df['Pertumbuhan Ekonomi (%)']},
    X='Tahun', Y='Pertumbuhan Ekonomi (%)', Markers='o', Template="seaborn"
)
pdrb = lineChart(
    Data={'Tahun':df['Tahun'], 'PDRB per Kapita (Juta Rp)':df['PDRB per Kapita (Juta Rp)']},
    X='Tahun', Y='PDRB per Kapita (Juta Rp)', Markers='o', Template="seaborn"
)
umkm = barChart(
    Data={'Tahun':df['Tahun'], 'Jumlah UMKM (Unit)':df['Jumlah UMKM (Unit)']},
    X='Tahun', Y='Jumlah UMKM (Unit)', Template="seaborn"    
)