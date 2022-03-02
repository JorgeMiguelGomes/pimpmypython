# -*- coding: utf-8 -*-
# author: Jorge Gomes 


import random
import pandas as pd 
import numpy as np 

# Import Dash and Dash Bootstrap Components
import dash
import dash_daq as daq
from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc
# _________________________________________

import plotly.express as px 



app = dash.Dash(
    external_stylesheets=[dbc.themes.CYBORG],
    #suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

app.layout = html.Div(
    dbc.Container(
    html.Div([
        html.H4('PIMP MY PYTHON'),
        html.Div(html.H4(id='ip')),
        html.Div(html.H2(id='a')),
        html.Div(id='b'),
        html.Div(id='c'),
        html.Div(id='d'),
        dcc.Graph(id='graph'),
        dcc.Interval(
            id='component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])
    )
)



@app.callback(
                Output(component_id="ip",component_property="children"),
                Output(component_id="a",component_property="children"),
                Output(component_id="b",component_property="children"),
                Output(component_id="c",component_property="children"),
                Output(component_id="d",component_property="children"),
                Output(component_id="graph",component_property="figure"),
                Input(component_id="component",component_property="n_intervals")
)



def update(component):
    a = str(random.randint(1, 254))
    b = str(random.randint(1, 254))
    c = str(random.randint(1, 254))
    d = str(random.randint(1, 254))
    dot = "."
    ip = a + dot + b + dot + c + dot + d



    a1 = str(random.randint(1, 1400))
    b1 = str(random.randint(1, 700))
    c1 = str(random.randint(1, 800))
    d1 = str(random.randint(1, 1240))

   
    fig = px.pie(names=['resistance','threath','exploit','profit'], values=[c1, d1, b1, d1], template='plotly_dark',hole=0.6, color_discrete_sequence=px.colors.sequential.Viridis)
    


    return ip,a,b,c,d,fig

if __name__ == "__main__":
    app.run_server(debug=True, port=8888)   

# END APP 





