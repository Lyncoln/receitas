# -*- coding: utf-8 -*-
"""
Created on Wed May  1 20:06:34 2019

@author: Lyncoln
"""
import dash_table
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from pesquisador import pesquisa


receitas = pd.read_csv("https://github.com/Lyncoln/receitas/raw/master/receitas.csv")
app = dash.Dash()

df = pd.DataFrame(columns = ["nome","ingredientes","site"])

app.layout = html.Div([html.H3("Entre os ingredientes:"),
        html.Div(children = [
        dcc.Input(id = "input", value = "", type = "text"),
        html.Div(id = "output")
        ]),
        dash_table.DataTable(id='table',
                             columns=[{"name": i, "id": i} for i in df.columns],
                             data=df.to_dict('records'))
])

@app.callback(Output(component_id="table", component_property = "data"),
        [Input(component_id = "input", component_property="value")])
def update_value(input_data):
    
    testo = input_data.split()
    tabela = pesquisa(testo)
    
    return tabela.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)
