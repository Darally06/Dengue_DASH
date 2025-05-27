from dash import html, dcc

def layout():
    return html.Div([
        dcc.Tabs([
            dcc.Tab(label='Definición del problema', children=[
                html.Div([
                    html.H3('Problema', 
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '30px'}),
                    html.P('Predecir si un caso debe ser confirmado como positivo para dengue o no, utilizando técnicas de aprendizaje automático',
                            style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                    html.H3('Variable objetivo',
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '30px'}),
                    html.P('CONFIRMADOS: indica si un caso es catalogado como probable o si se confirma la presencia del virus por laboratorio o por nexo epidemiológico',
                            style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                    html.H3('Importancia del problema',
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '30px'}),
                    html.Ul([
                        html.Li('🔹Reducir la cantidad de falsos negativos para evitar diagnósticos erróneos.'),
                        html.Li('🔹Optimizar recursos médicos y focalizar esfuerzos en los casos reales.'),
                    ], style={'fontFamily': 'Century Gothic', 'fontSize': '24px','listStyleType': 'none','paddingLeft': '0px','lineHeight': '1.8'})
                ])
            ]),

            dcc.Tab(label='Preparación de Datos', children=[
                html.Div([
                    html.H3('Lectura de los datos', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '30px'}),
                    html.P('Se utilizó un archivo CSV con registros clínicos y demográficos de casos de dengue.', style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                    
                    html.H3('Limpieza y transformación de datos', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '30px'}),
                    html.Ul([
                        html.Li('🔹 Eliminar variables irrelevantes o redundantes.'),
                        html.Li('🔹 Conversión de la variable EDAD a unidad de medida años'),
                        html.Li('🔹 Imputación de valores faltantes utilizando la mediana'),
                        html.Li('🔹 Codificación de variables categóricas ')
                    ], style={'fontFamily': 'Century Gothic', 'fontSize': '24px','listStyleType': 'none','paddingLeft': '0px','lineHeight': '1.8'}),
                    
                    html.H3('División de los datos', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '30px'}),
                    html.P('División estratificada de datos: 60% entrenamiento - 40% Test', style={'fontFamily': 'Century Gothic', 'fontSize': '24px'})
                    ])
            ]),

            dcc.Tab(label='Selección del modelo', children=[
                html.Div([
                    html.H3('Modelo elegido', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '30px'}),
                    html.H3('SD-GBClassifier', style={'textAlign': 'center', 'color': '#1f4e79', 'fontFamily': 'Poppins', 'fontSize': '30px'}),
                    html.P('Modelo con ensamblado tipo stacking que combina los modelos Random Forest y XGBoost para entrenar un meta-modelo Gradient Boosting',
                            style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                    
                    html.H3('Justificación', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '30px'}),
                    html.P('Un enfoque de ensamble combina las fortaleza de los modelos base para dar solución a la tarea de optimización.',
                           style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                    
                    html.H3('Configuración del modelo', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '30px'}),
                    html.Ul([
                        html.Li('🔹 Usando validación cruzada se encontraron los mejores hiperparámetros para los modelos base.'),
                        html.Li('🔹 Se entrenó el meta-modelo con configuración passtrough = True'),
                    ], style={'fontFamily': 'Century Gothic', 'fontSize': '24px','listStyleType': 'none','paddingLeft': '0px','lineHeight': '1.8'}),
                ])
            ]),

            dcc.Tab(label='Evaluación del modelo', children=[
                html.Div([
                    html.H3('Entrenamiento', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '30px'}),
                    html.P('El modelo fue entrenado sobre el conjunto de entrenamiento tomando un 70% de los datos (663,096 registros)',
                           style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                    html.P('Tiempo de entrenamiento: 6.74 minutos',
                        style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                           
                    html.H3('Métricas de evaluación', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '30px'}),
                    html.Ul([
                        html.Li('🔹 Recall: 0.8259 '),
                        html.Li('🔹 F1-Score: 0.7725 '),
                        html.Li('🔹 ROC AUC: 0.8543'),
                    ], style={'fontFamily': 'Century Gothic', 'fontSize': '24px','listStyleType': 'none','paddingLeft': '0px','lineHeight': '1.8'}),
                ])
            ]),
        ])
    ])

