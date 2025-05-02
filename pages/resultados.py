from dash import html, dcc, dash_table
import pandas as pd
import os
import json
import plotly.io as pio

def eda(df):
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

def mostrar_json(path_json):
    if not os.path.exists(path_json):
        return html.Div("Archivo no encontrado")
    with open(path_json, 'r') as f:
        fig_dict = json.load(f)
    fig = pio.from_json(json.dumps(fig_dict))
    return dcc.Graph(figure=fig)

def layout(df):
    return html.Div([
        dcc.Tabs([

            # Pestaña 1: EDA
            dcc.Tab(label='Análisis Exploratorio de Datos', children=[
               eda(df)
            ]),

            # Pestaña 2: Modelo
            dcc.Tab(label='Visualización del modelo', children=[
                html.Div([
                    html.Div([
                        html.H4("Curva ROC",style={'textAlign': 'center'}),
                        mostrar_json(r"pages\resultados\graficas\ROC_AUC.json")
                    ], style={'width': '48%', 'padding': '1%', 'boxSizing': 'border-box'}),
                    
                    html.Div([
                        html.H4("Curva Precision-Recall",style={'textAlign': 'center'}),
                        mostrar_json(r"pages\resultados\graficas\precision_recall_curve.json")
                    ], style={'width': '48%', 'padding': '1%', 'boxSizing': 'border-box'}),
                    
                    html.Div([
                        html.H4("Importancia de características",style={'textAlign': 'center'}),
                        mostrar_json(r"pages\resultados\graficas\feat_importance.json")
                    ], style={'width': '48%', 'padding': '1%', 'boxSizing': 'border-box'}),
                    
                    html.Div([
                        html.H4("Explicación LIME",style={'textAlign': 'center'}),
                        mostrar_json(r"pages\resultados\graficas\lime.json"),
                    ], style={'width': '48%', 'padding': '1%', 'boxSizing': 'border-box'}),
                ], style={
                    'display': 'flex','flexWrap': 'wrap','justifyContent': 'space-around','alignItems': 'flex-start'
                }),
            ]),

            # Pestaña 3: indicadores
            dcc.Tab(label='Indicadores del modelo', children=[
                html.Div([
                    html.Div([
                        html.H4("Matriz de Confusión", style={'textAlign': 'center'}),
                        mostrar_json(r"pages\resultados\graficas\matriz_confusion.json"),
                    ], style={'width': '48%', 'padding': '1%', 'boxSizing': 'border-box'}),

                    html.Div([
                        html.H4("Reporte de Clasificación", style={'textAlign': 'center'}),
                        html.Pre(
                            open(r"pages\resultados\class_report.txt").read(),
                            style={'whiteSpace': 'pre-wrap'}
                        )
                    ], style={'width': '48%', 'padding': '1%', 'boxSizing': 'border-box'}),
                ], style={
                    'display': 'flex',
                    'flexWrap': 'wrap',
                    'justifyContent': 'space-around',
                    'alignItems': 'flex-start'
                }),
            ]),


            # Pestaña 4: Limitaciones
            dcc.Tab(label='Limitaciones', children=[
                html.Div('Aqui', style={'marginTop': '20px'})
            ]),
        ])
    ])