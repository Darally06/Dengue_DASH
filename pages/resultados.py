import json
import requests
import dash
from dash import dcc, html, Input, Output
import plotly.io as pio

# ----------------
# URLs de los gráficos
url_area = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_area.json"
url_confirma = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_confirma.json" 
url_decesos = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_decesos.json" 
url_dptos = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_dptos.json" 
url_edad = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_edad.json" 
url_eventos_y = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_eventos_y.json" 
url_hosp_sex = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_hosp_sex.json" 
url_muns = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_muns.json" 
url_seguro ="https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_seguro.json" 
url_semana = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_semana.json" 
url_sexo = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_sexo.json"  
url_tip_cas = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_tip_cas.json" 
url_mapa = "/assets/mapa_deptos.html"
url_rocauc = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/ROC_AUC.json" 
url_presrecall = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/precision_recall_curve.json" 
url_imp_rf = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/base_feat_importance_rf.json" 
url_imp_xg = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/base_feat_importance_xgb.json" 
url_matriz = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/matriz_confusion.json" 
url_lime = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/lime_SD-GBClassifier_1000.json"
                                                                                                 

def cargar_grafico(url):
    try:
        if url:
            response = requests.get(url)
            response.raise_for_status()
            fig_dict = json.loads(response.content)
            fig = pio.from_json(response.text)
        else:
            raise ValueError("Debe proporcionar una URL o un tipo de gráfico.")
        return dcc.Graph(figure=fig, config={"displayModeBar": False})
    except Exception as e:
        return html.Div([
            html.P(f"Error al cargar gráfico: {e}", style={"color": "red"})
        ])

def layout():
    return html.Div([
        dcc.Tabs([

            # Pestaña 1: EDA
            dcc.Tab(label='Análisis Exploratorio de Datos', children=[
                html.Div([
                    dcc.Tabs(id='eda-tabs', value='Demográficas', children=[
                        dcc.Tab(label='Demográficas', value='Demográficas'),
                        dcc.Tab(label='Temporales', value='Temporales'),
                        dcc.Tab(label='Geográficas', value='Geográficas'),
                        dcc.Tab(label='Clínicas', value='Clínicas'),
                    ]),
                    html.Div(id='contenido-graficos')
                ])
            ]),

            # Pestaña 2: Modelo
            dcc.Tab(label='Visualización del modelo', children=[
                html.Div([
                    html.Div([
                        html.H4("Curva ROC", style={'textAlign': 'center'}),
                        dcc.Loading(children=[cargar_grafico(url_rocauc)])
                    ], style={'width': '48%', 'padding': '1%'}),

                    html.Div([
                        html.H4("Curva Precision-Recall", style={'textAlign': 'center'}),
                        dcc.Loading(children=[cargar_grafico(url_presrecall)])
                    ], style={'width': '48%', 'padding': '1%'}),

                    html.Div([
                        html.H4("Importancia de características (Random Forest)", style={'textAlign': 'center'}),
                        dcc.Loading(children=[cargar_grafico(url_imp_rf)])
                    ], style={'width': '48%', 'padding': '1%'}),

                    html.Div([
                        html.H4("Importancia de características (XGBoost)", style={'textAlign': 'center'}),
                        dcc.Loading(children=[cargar_grafico(url_imp_xg)])
                    ], style={'width': '48%', 'padding': '1%'}),
                ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-around'})
            ]),

            # Pestaña 3: Indicadores del modelo
            dcc.Tab(label='Indicadores del modelo', children=[
                html.Div([
                    html.Div([
                        html.H4("Matriz de Confusión", style={'textAlign': 'center'}),
                        cargar_grafico(url_matriz)
                    ], style={'width': '48%', 'padding': '1%'}),

                    html.Div([
                        html.H4("Reporte de Clasificación", style={'textAlign': 'center'}),
                        html.Pre(open("pages/class_report.txt").read(), style={'whiteSpace': 'pre-wrap'})
                    ], style={'width': '48%', 'padding': '1%'}),

                    html.Div([
                        html.H4("Importancia de características", style={'textAlign': 'center'}),
                        cargar_grafico(url_lime)
                    ], style={'width': '48%', 'padding': '1%'})
                ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-around'})
            ]),

            # Pestaña 4: Limitaciones
            dcc.Tab(label='Limitaciones', children=[
                html.Div([
                    html.H4("Limitaciones del modelo", style={'textAlign': 'center'}),
                    html.Div([
                        html.Ul([
                            html.Li("Falta de variables: no se cuentan con registros record clínicos " \
                            "que permintan realizar análisis más profundos"),
                            html.Li("Falsos positivos: Aunque se redujo notablemente en comparación con " \
                            "los otros modelos, obtener 29.7% sigue siendo alto"),
                        ], style={'fontFamily': 'Lato', 'fontSize': '18px', 'lineHeight': '1.6'})
                    ], style={'width': '50%', 'float': 'right', 'paddingRight': '2%'})
                ])
            ])
        ])
    ])

def register_callbacks(app):
    @app.callback(
        Output('contenido-graficos', 'children'),
        Input('eda-tabs', 'value')
    )

    def update_eda(selected_group):
        if selected_group == 'Demográficas':
            # Ensamblar en columnas
            return html.Div([
                html.Div([
                    cargar_grafico(url_edad)
                ], style={'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top'}),

                html.Div([
                    html.Div([
                        html.Div([
                            cargar_grafico(url_area)
                        ], style={'width': '40%', 'paddingRight': '4%'}),

                        html.Div([
                            cargar_grafico(url_sexo)
                        ], style={'width': '40%'})
                    ], style={'display': 'flex', 'justifyContent': 'space-between'}),

                    html.Div([
                        cargar_grafico(url_seguro)
                    ], style={'marginTop': '-75px'})
                ], style={'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top'})
            ])

        elif selected_group == 'Temporales':
            return html.Div([
                html.Div([
                    cargar_grafico(url_semana)
                ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top', 'paddingRight': '2%'}),

                html.Div([
                    cargar_grafico(url_confirma)
                ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'})
            ])
            
        elif selected_group == 'Geográficas':
            return html.Div([
                html.Div([
                    # Gráficos laterales
                    html.Div([
                        html.Div([
                            html.H4("Top 5 Departamentos con más casos"),
                            cargar_grafico(url_dptos)
                        ], style={"marginBottom": "40px"}),

                        html.Div([
                            html.H4("Top 5 Municipios con más casos"),
                            cargar_grafico(url_muns)
                        ])
                    ], style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top'}),

                    # Mapa de densidad
                    html.Div([
                        html.H4("Mapa de Densidad de Casos por Departamento", style={"textAlign": "center"}),

                        html.Iframe(
                            id='mapa-dengue',
                            src=url_mapa,
                            width='100%',
                            height='800px',
                            style={"border": "none"}
                        )
                    ], style={'width': '58%', 'display': 'inline-block', 'paddingLeft': '2%'})
                ])
            ])
        elif selected_group == 'Clínicas':
            return html.Div([
                html.Div([
                    html.Div([
                        cargar_grafico(url_eventos_y)
                    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

                    html.Div([
                        cargar_grafico(url_tip_cas)
                    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top', 'paddingLeft': '4%'})
                ]),

                html.Div([
                    html.Div([
                        cargar_grafico(url_hosp_sex)
                    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

                    html.Div([
                        cargar_grafico(url_decesos)
                    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top', 'paddingLeft': '4%'})
                ])
            ])
        else:
            return html.Div("Seleccione una categoría válida.")
