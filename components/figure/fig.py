import plotly.express as px 
import pandas as pd

def lineChart(Data,X,Y,Markers,Template):
    fig = px.line(
        data_frame=pd.DataFrame(Data),
        x=X, y=Y, markers=Markers, template=Template
    )
    return fig

def barChart(Data,X,Y,Template):
    fig = px.bar(
        data_frame=pd.DataFrame(Data),
        x=X, y=Y, template=Template
        )
    return fig

def pieChart(Data,Name,Values, Template):
    fig = px.pie(
        data_frame=pd.DataFrame(Data),
        names=Name, values=Values, template=Template
    )
    return fig

def radarChart(Data,R,Theta,Template):
    fig = px.bar_polar(
        data_frame=pd.DataFrame(Data),
        r=R, theta=Theta, template=Template
    )
    fig.update_traces(
        fill='toself'
    )
    fig.update_layout(
        polar=dict(
            angularaxis=dict(
                type="category", gridcolor="#e0e0e0"),
            radialaxis=dict(
                showticklabels=False, gridcolor="#e0e0e0"
            ), 
        )
    )
    return fig