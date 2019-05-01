# -*- coding: utf-8 -*-
"""
Created on Wed May  1 20:06:34 2019

@author: Lyncoln
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children = [
        dcc.Input(id = "input", value = "Enter something", type = "text"),
        html.Div(id = "output")
        ])

@app.callback(Output(component_id="output", component_property = "children"),
        [Input(component_id = "input", component_property="value")])
def update_value(input_data):
    return "Input: {}".format(input_data)

if __name__ == '__main__':
    app.run_server(debug=True)