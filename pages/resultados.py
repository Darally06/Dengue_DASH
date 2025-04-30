from dash import html, dcc
import pandas as pd

def eda(df):
    print(df.info())
    return html.Div([
        html.Div([
            dcc.Tabs([
                dcc.Tab(label="Demograficas", children = [
                    html.Div([
                        html.P('Aqui van los graficos 1')
                    ])
                ]),
                dcc.Tab(label="temporal", children = [
                    html.Div([
                        html.P('Aqui van los graficos 1')
                    ])
                ]),
                dcc.Tab(label="Geograficas", children = [
                    html.Div([
                        html.P('Aqui van los graficos 1')
                    ])
                ]),
                dcc.Tab(label="clinicas", children = [
                    html.Div([
                        html.P('Aqui van los graficos 1')
                    ])
                ]),
            ], vertical=True)
        ], style={'margin-left': '20%', 'width': '80%', 'padding': '20px'})
    ])



def layout(df):
    return html.Div([
        dcc.Tabs([
            dcc.Tab(label='Análisis Exploratorio de Datos', children=[
               eda(df)
            ]),
            dcc.Tab(label='Visualización del modelo', children=[
                html.Div('Aqui', style={'marginTop': '20px'})
            ]),
            dcc.Tab(label='Indicadores del modelo', children=[
                html.Div('Aqui', style={'marginTop': '20px'})
            ]),
            dcc.Tab(label='Limitaciones', children=[
                html.Div('Aqui', style={'marginTop': '20px'})
            ]),
        ]),
    ])

