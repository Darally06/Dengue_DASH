from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
from unidecode import unidecode
import plotly.graph_objects as go
from pages.resultados import cargar_grafico

url_area = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_area.json"
url_confirma = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_confirma.json"
url_decesos = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_decesos.json"
url_dptos = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_dptos.json"
url_edad = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_edad.json"
url_eventos_y = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_eventos_y.json"
url_hosp_sex = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_hosp_sex.json"
url_muns = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_muns.json"
url_seguro = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_seguro.json"
url_semana = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_semana.json"
url_sexo = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_sexo.json"
url_tip_cas = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_tip_cas.json"
url_mapa = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/mapa_dengue.html"


def register(app):
    @app.callback(
        Output('eda-content', 'children'),
        Input('eda-selector', 'value'),
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
   