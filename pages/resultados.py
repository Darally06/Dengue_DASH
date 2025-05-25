from dash import html, dcc, Input, Output
import plotly.express as px
import os
import json
import plotly.io as pio
import requests

def cargar_grafico(url_json):
    try:
        response = requests.get(url_json)
        response.raise_for_status()  # Lanza error si la URL no es válida

        fig_dict = response.json()
        fig = pio.from_json(json.dumps(fig_dict))  # Convertir dict a JSON string

        return dcc.Graph(figure=fig)
    except Exception as e:
        return html.Div(f"⚠️ Error al cargar el gráfico: {str(e)}")

def layout():
    return html.Div([
        dcc.Tabs([
            dcc.Tab(label='Análisis Exploratorio de Datos', children=[
                html.Div([
                    dcc.Dropdown(
                        id='eda-selector',
                        options=[
                            {'label': 'Demográficas', 'value': 'Demográficas'},
                            {'label': 'Temporales', 'value': 'Temporales'},
                            {'label': 'Geográficas', 'value': 'Geográficas'},
                            {'label': 'Clínicas', 'value': 'Clínicas'}
                        ],
                        value='Demográficas',
                        clearable=False,
                        style={'width': '60%', 'marginBottom': '20px'}
                    ),
                    html.Div(id='eda-content')
                ])
            ]),
            # Pestaña 2: Modelo
            dcc.Tab(label='Visualización del modelo', children=[
                html.Div([
                    html.Div([
                        html.H4("Curva ROC", style={'textAlign': 'center'}),
                        dcc.Loading(
                            children=cargar_grafico("https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/ROC_AUC.json"),
                            type="default"
                        )
                    ], style={'width': '48%', 'padding': '1%', 'boxSizing': 'border-box'}),

                    html.Div([
                        html.H4("Curva Precision-Recall", style={'textAlign': 'center'}),
                        dcc.Loading(
                            children=cargar_grafico("https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/precision_recall_curve.json"),
                            type="default"
                        )
                    ], style={'width': '48%', 'padding': '1%', 'boxSizing': 'border-box'}),

                    html.Div([
                        html.H4("Importancia de características (Random Forest)", style={'textAlign': 'center'}),
                        dcc.Loading(
                            children=cargar_grafico("https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/base_feat_importance_rf.json"),
                            type="default"
                        )
                    ], style={'width': '48%', 'padding': '1%', 'boxSizing': 'border-box'}),

                    html.Div([
                        html.H4("Importancia de características (XGBoost)", style={'textAlign': 'center'}),
                        dcc.Loading(
                            children=cargar_grafico("https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/base_feat_importance_xgb.json"),
                            type="default"
                        )
                    ], style={'width': '48%', 'padding': '1%', 'boxSizing': 'border-box'}),
                ], style={
                    'display': 'flex', 'flexWrap': 'wrap',
                    'justifyContent': 'space-around', 'alignItems': 'flex-start'
                }),
            ]),

            dcc.Tab(label='Indicadores del modelo', children=[
                html.Div([
                    html.Div([
                        html.H4("Matriz de Confusión", style={'textAlign': 'center'}),
                        cargar_grafico("https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/matriz_confusion.json"),
                    ], style={'width': '48%', 'padding': '1%', 'boxSizing': 'border-box'}),

                    html.Div([
                        html.H4("Reporte de Clasificación", style={'textAlign': 'center'}),
                        html.Pre(
                            open(r"pages\class_report.txt").read(),
                            style={'whiteSpace': 'pre-wrap'}
                        )
                    ], style={'width': '48%', 'padding': '1%', 'boxSizing': 'border-box'}),
                    html.Div([
                        html.H4("Importancia de características", style={'textAlign': 'center'}),
                        cargar_grafico("https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/lime_SD-GBClassifier_1000.json"),
                    ], style={'width': '48%', 'padding': '1%', 'boxSizing': 'border-box'}),
                ], style={
                    'display': 'flex',
                    'flexWrap': 'wrap',
                    'justifyContent': 'space-around',
                    'alignItems': 'flex-start'
                }),
            ]),
            dcc.Tab(label='Limitaciones', children=[
                html.Div([
                    html.H4("Limitaciones del modelo", style={'textAlign': 'center'}),
                    html.P('1. Desbalance de clases: A pesar de aplicar SMOTE, el desbalance de clases puede afectar la capacidad del modelo para generalizar.'\
                            '2. El tiempo de ejecución es considerablemente alto, lo que puede dificultar la implementación en tiempo real.',
                            style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                ])
            ]),
        ])
    ])
