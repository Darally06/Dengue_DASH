from dash import html, dcc, Input, Output, dash_table
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import json
from unidecode import unidecode 
import folium

def register(app, df):
    @app.callback(
        Output('eda-content', 'children'),
        Input('eda-selector', 'value')
    )
    
    
    def update_eda(selected_group):
        if selected_group == 'Demográficas':
            # Boxplot de edad ajustada
            fig_edad = px.box(df, x="EDAD_AJUSTADA")
            fig_edad.update_layout(
                title="Distribución de la Edad",
                xaxis_title="Edad",
                yaxis_title="Frecuencia",
                height=650,
                margin=dict(l=20, r=20, t=50, b=50),
                title_font=dict(size=18, family='Lato', color='black'),
                xaxis=dict(showgrid=False),  # Ocultar cuadrícula en eje X
                yaxis=dict(showgrid=False),  # Ocultar cuadrícula en eje Y
                plot_bgcolor="white"
            )
            fig_edad.update_traces(marker=dict(color="dodgerblue"))

            # Gráfico de pastel para sexo
            sexo_data = df["SEXO_NUM"].replace({0: "Mujer", 1: "Hombre"}).value_counts().reset_index()
            sexo_data.columns = ["Sexo", "Cantidad"]
            fig_sexo = px.pie(
                sexo_data,
                names='Sexo',
                values='Cantidad',
                title='Distribución por Sexo',
                color_discrete_sequence=["#F54B70", "#4B70F5"]
            )
            fig_sexo.update_traces(
                textposition='inside',
                textinfo='percent+label',
                pull=[0.02]*len(sexo_data),
                sort=False
            )
            fig_sexo.update_layout(
                showlegend=True,
                legend=dict(orientation='h', y=-0.15, x=0.25),
                margin=dict(t=50, b=50, l=20, r=20),
                height=350
            )

            # Gráfico de pastel para área
            area_data = df["AREA"].value_counts().reset_index()
            area_data.columns = ["Área", "Cantidad"]
            fig_area = px.pie(
                area_data,
                names='Área',
                values='Cantidad',
                title='Distribución por Área',
                color_discrete_sequence=["#4B70F5", "#0D3CE7", "#93AAF9"]
            )
            fig_area.update_traces(
                textposition='inside',
                textinfo='percent+label',
                pull=[0.02]*len(area_data),
                sort=False
            )
            fig_area.update_layout(
                showlegend=True,
                legend=dict(orientation='h', y=-0.15, x=0.25),
                margin=dict(t=50, b=50, l=20, r=20),
                height=350
            )


            # Gráfico de barra horizontal para tipo de seguro
            seguro_data = df["TIP_SS"].value_counts().reset_index()
            seguro_data.columns = ["Tipo de Seguro", "Cantidad"]
            fig_seguro = px.bar(seguro_data, x="Cantidad", y="Tipo de Seguro", orientation='h',
                                title="Distribución por Tipo de Seguro",
                                color_discrete_sequence=["#4B70f5"])
            fig_seguro.update_layout(yaxis_title="", xaxis_title="Cantidad", plot_bgcolor="white")

            return html.Div([
            html.Div([
                dcc.Graph(figure=fig_edad)
            ], style={'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top'}),

            html.Div([
                html.Div([
                    html.Div([
                        dcc.Graph(figure=fig_area)
                    ], style={'width': '40%', 'paddingRight': '4%'}),

                    html.Div([
                        dcc.Graph(figure=fig_sexo)
                    ], style={'width': '40%'})
                ], style={'display': 'flex', 'justifyContent': 'space-between'}),

                html.Div([
                    dcc.Graph(figure=fig_seguro)
                ], style={'marginTop': '-75px'})
            ], style={'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top'})
        ])



        elif selected_group == 'Temporales':
            # Gráfico 1: Casos por semana y año
            conteo_semanal_anual = df.groupby(["ANO", "SEMANA"]).size().unstack(level=0, fill_value=0)
            fig_semana = go.Figure()
            for año in conteo_semanal_anual.columns:
                fig_semana.add_trace(go.Scatter(
                    x=conteo_semanal_anual.index,
                    y=conteo_semanal_anual[año],
                    mode="lines",
                    name=str(año),
                    line=dict(width=2)
                ))

            fig_semana.update_layout(
                title="Casos de Dengue por Semana y Año",
                xaxis_title="Semana",
                yaxis_title="Número de Casos",
                template="plotly_white",
                hovermode="x unified",
                legend_title="Año",
                font=dict(family='Roboto, Arial, sans-serif')
            )

            # Gráfico 2: Casos confirmados por año (convertido a líneas)
            df["CONFIRMADOS"] = df["CONFIRMADOS"].map({0: "No", 1: "Sí"})
            df_conf = df.groupby(["ANO", "CONFIRMADOS"]).size().reset_index(name="Frecuencia")

            fig_cf = px.line(
                df_conf,
                x="ANO",
                y="Frecuencia",
                color="CONFIRMADOS",
                title="Distribución de Casos Confirmados por Año",
                height=600,
                labels={"ANO": "Año", "Frecuencia": "Número de Casos", "CONFIRMADOS": "Confirmados"},
                color_discrete_map={"No": "deepskyblue", "Sí": "blue"},
                markers=True
            )

            fig_cf.update_layout(
                template="plotly_white",
                hovermode="x unified",
                legend_title="Confirmados",
                font=dict(family='Roboto, Arial, sans-serif')
            )

            return html.Div([
                html.Div([
                    dcc.Graph(figure=fig_semana)
                ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top', 'paddingRight': '2%'}),

                html.Div([
                    dcc.Graph(figure=fig_cf)
                ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'})
            ])


        elif selected_group == 'Geográficas':
        
            # Cargar archivo de población por departamento
            deptos = pd.read_csv("data\poblacion_departamentos_colombia_2018.csv")
            deptos.rename(columns={"Población Censada 2018": "Poblacion"}, inplace=True)
            deptos["DEPARTAMENTO"] = deptos["DEPARTAMENTO"].apply(lambda x: unidecode(x.upper()))
            deptos["DEPARTAMENTO"] = deptos["DEPARTAMENTO"].replace({
                "SAN ANDRES, PROVIDENCIA Y SANTA CATALINA": "ARCHIPIELAGO DE SAN ANDRES, PROVIDENCIA Y SANTA CATALINA"
            })

            # Casos por departamento
            df["DPTO_OCU"] = df["DPTO_OCU"].apply(lambda x: unidecode(x.upper()))
            casos_por_dpto = df["DPTO_OCU"].value_counts().reset_index()
            casos_por_dpto.columns = ["DEPARTAMENTO", "Casos"]
            df_final = pd.merge(casos_por_dpto, deptos, on="DEPARTAMENTO", how="left")
            df_final["Densidad_Casos"] = (df_final["Casos"] / df_final["CENSO"]) * 100000
            df_final = df_final.sort_values(by="Densidad_Casos", ascending=False)

            # Cargar GeoJSON
            with open("data\Mapa_Depto.geojson", encoding="utf-8") as f:
                geojson = json.load(f)

            # Asignar densidad y casos a cada feature
            for feature in geojson["features"]:
                dpto = unidecode(feature["properties"]["dpto_cnmbr"].upper())
                match = df_final[df_final["DEPARTAMENTO"] == dpto]
                if not match.empty:
                    feature["properties"]["casos"] = int(match["Casos"].values[0])
                    feature["properties"]["densidad"] = round(match["Densidad_Casos"].values[0], 2)
                else:
                    feature["properties"]["casos"] = 0
                    feature["properties"]["densidad"] = 0

            # Crear mapa
            m = folium.Map(location=[4.5709, -74.2973], zoom_start=5)
            choropleth = folium.Choropleth(
                geo_data=geojson,
                name="Choropleth",
                data=df_final,
                columns=["DEPARTAMENTO", "Densidad_Casos"],
                key_on="feature.properties.dpto_cnmbr",
                fill_color="Blues",
                fill_opacity=0.7,
                line_opacity=0.2,
                legend_name="Densidad de Casos por 100,000 Habitantes",
                nan_fill_color="white"
            ).add_to(m)

            folium.GeoJsonTooltip(
                fields=["dpto_cnmbr", "casos", "densidad"],
                aliases=["Departamento:", "Casos:", "Densidad:"],
                localize=True,
                sticky=False,
                labels=True,
                style="background-color: white; color: black; font-size: 12px; padding: 5px;",
            ).add_to(choropleth.geojson)

            m.save("mapa_dengue.html")

            #Top 5 departamentos con más casos
            
            top5_dptos = df["DPTO_OCU"].value_counts().nlargest(5)
            fig_dptos = go.Figure(go.Bar(
                x=top5_dptos.values,
                y=top5_dptos.index,
                orientation='h',
                marker=dict(color='#0D3CE7')
            ))
            fig_dptos.update_layout(
                title="Top 5 Departamentos con más casos",
                xaxis_title="Número de casos",
                yaxis_title="Departamento",
                template="plotly_white",
                height=350,
                margin=dict(l=100, r=40, t=50, b=40)
            )
            
            #Top 5 municipios con más casos
            
            top5_muns = df["MUN_OCU"].value_counts().nlargest(5)
            fig_muns = go.Figure(go.Bar(
                x=top5_muns.values,
                y=top5_muns.index,
                orientation='h',
                marker=dict(color='#4B70F5')
            ))
            fig_muns.update_layout(
                title="Top 5 Municipios con más casos",
                xaxis_title="Número de casos",
                yaxis_title="Municipio",
                template="plotly_white",
                height=350,
                margin=dict(l=100, r=40, t=50, b=40)
            )

            # Leer HTML del mapa guardado previamente
            mapa_html = open("mapa_dengue.html", 'r', encoding='utf-8').read()

            return html.Div([
                html.Div([
                    # Gráficos laterales
                    html.Div([
                        html.Div([
                            html.H4("Top 5 Departamentos con más casos"),
                            dcc.Graph(figure=fig_dptos)  # Debes tener esta figura preparada
                        ], style={"marginBottom": "40px"}),

                        html.Div([
                            html.H4("Top Municipios con más casos"),
                            dcc.Graph(figure=fig_muns)
                        ])
                    ], style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top'}),

                    # Mapa de densidad
                    html.Div([
                        html.H4("Mapa de Densidad de Casos por Departamento", style={"textAlign": "center"}),
                        html.Iframe(
                            id='mapa-dengue',
                            srcDoc=mapa_html,
                            width='100%',
                            height='800px',
                            style={"border": "none"}
                        )
                    ], style={'width': '58%', 'display': 'inline-block', 'paddingLeft': '2%'})
                ])
            ])

        elif selected_group == 'Clínicas':

            # 1. EVENTOS X AÑO (Barras)
            df_eventos = df.groupby(["ANO", "EVENTO"]).size().reset_index(name="Pacientes")
            fig_eve_y = px.bar(
                df_eventos,
                x="ANO",
                y="Pacientes",
                color="EVENTO",
                title="Pacientes por Evento y Año",
                labels={"ANO": "Año", "Pacientes": "Número de Pacientes"},
                barmode="group",  # Agrupa las barras por año
                color_discrete_map={"DENGUE": "dodgerblue", "DENGUE GRAVE": "mediumblue"}
            )
            fig_eve_y.update_layout(
                xaxis=dict(tickmode="linear"),
                legend_title="Evento",
                hovermode="x unified",
                template="plotly_white"
            )


            # 2. TIPO_CASO x AÑO (Línea)
            df_tipo_caso = df.groupby(["ANO", "TIP_CAS"]).size().reset_index(name="Frecuencia")
            fig_tip_cas = px.line(
                df_tipo_caso,
                x="ANO",
                y="Frecuencia",
                markers=True,
                title="Tipo de Caso por Año",
                labels={"ANO": "Año", "Frecuencia": "Número de Casos", "TIP_CAS": "Tipo de Caso"},
            )
            fig_tip_cas.update_traces(line=dict(color="#1b4af2"))
            fig_tip_cas.update_layout(
                template="plotly_white",
                hovermode="x unified",
                legend_title="Tipo de Caso"
            )

            # 3. HOSPITALIZADOS POR AÑO Y SEXO (Línea)
            
            df['SEXO_L'] = df['SEXO_NUM'].replace({0: 'Mujer', 1: 'Hombre'})
            # Agrupar por año y sexo para hospitalizados
            df_hosp_sex = df[df['PAC_HOS'] == 1].groupby(['ANO', 'SEXO_L']).size().reset_index(name='Frecuencia')

            fig_hosp_sex = px.line(
                df_hosp_sex,
                x='ANO',
                y='Frecuencia',
                color='SEXO_L',
                title='Pacientes Hospitalizados por Año y Sexo',
                markers=True,
                labels={
                    'ANO': 'Año',
                    'Frecuencia': 'Pacientes Hospitalizados',
                    'SEXO_L': 'Sexo'
                },
                color_discrete_map={'Hombre': '#4B70F5', 'Mujer': '#F54B70'}
            )

            fig_hosp_sex.update_layout(
                template='plotly_white',
                hovermode='x unified',
                legend_title='Sexo',
                margin=dict(t=50, b=50, l=30, r=30),
                height=400
            )


            # 4. DECESO X AÑO (Barras)
            df_decesos_año = df[df["CON_FIN"] == 2].groupby("ANO").size().reset_index(name="Decesos")
            fig_decesos = px.bar(
                df_decesos_año,
                x="ANO",
                y="Decesos",
                title="Decesos por Año",
                labels={"ANO": "Año", "Decesos": "Número de Fallecimientos"},
                color_discrete_sequence=["dodgerblue"]
            )
            fig_decesos.update_layout(
                template="plotly_white",
                hovermode="x unified"
            )

            return html.Div([
                html.Div([
                    html.Div([
                        dcc.Graph(figure=fig_eve_y)
                    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

                    html.Div([
                        dcc.Graph(figure=fig_tip_cas)
                    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top', 'paddingLeft': '4%'})
                ]),

                html.Div([
                    html.Div([
                        dcc.Graph(figure=fig_hosp_sex)
                    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

                    html.Div([
                        dcc.Graph(figure=fig_decesos)
                    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top', 'paddingLeft': '4%'})
                ])
            ])


        return html.Div("Selecciona una categoría para ver los gráficos.")
