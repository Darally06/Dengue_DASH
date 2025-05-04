from dash import html, dcc, Input, Output
import plotly.express as px
import os
import json
import plotly.io as pio

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
                        style={'width': '50%', 'marginBottom': '20px'}
                    ),
                    html.Div(id='eda-content')
                ])
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
