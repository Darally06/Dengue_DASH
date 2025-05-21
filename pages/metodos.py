from dash import html, dcc

def layout():
    return html.Div([
        dcc.Tabs([
            dcc.Tab(label='Definición del problema', children=[
                html.Div([
                    html.H3('Problema', 
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Predecir si un caso registrado en la base de datos debe ser confirmado'\
                            'como positivo para dengue o no, utilizando técnicas de aprendizaje automático',
                            style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                    html.H3('Variable objetivo',
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('La variable objetivo es CONFIRMADOS, que indica si un caso fue finalmente confirmado' \
                        'como positivo por laboratorio o por nexo epidemiológico "True" o no "False" para dengue. '\
                        'Este es un problema de clasificación binaria, con clases desbalanceadas.',
                        style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                    html.H3('Importancia del problema',
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Reducir la cantidad de falsos positivos y negativos para evitar diagnosticos erróneos,' \
                        'optimizar recursos médicos y focalizar esfuerzos en los casos reales.' \
                        'Por ello, el modelo debe priorizar un buen recall sin comprometer excesivamente la precisión',
                        style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                ])
            ]),
            dcc.Tab(label='Preparación de Datos', children=[
                html.Div([
                    html.H3('Lectura de los datos',
                             style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Se utilizó un archivo CSV con registros clínicos y demográficos de casos de dengue.',
                        style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                    html.H3('Limpieza y transformación de datos',
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.Ul([
                        html.Li('Eliminar variables irrelevantes o redundantes.'),
                        html.Li('Conversión de la variable edad a unidad de medida años, tomando 1 año como valor mínimo. ' \
                        'Se realizó inputación de valores faltantes utilizando la mediana'\
                        'La variable EDAD_AJUSTADA fue escalada mediante StandardScaler.'),
                        html.Li('Aplicación de One-Hot Encodig para las variables categoricas TIP_SS y EVENTO'),
                        html.Li('Para PAIS_OCU, DPTO_OCU, MUN_OCU, se utilizó codificación por frecuencia relativa.'),
                    ], style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                    html.H3('Desbalance de clases',
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Luego de aplicar una prueba de proporción, se determinó que la variable objetivo presenta un desbalance significativo entre las clases. '\
                           'Por lo tanto, se aplicó la técnica de sobremuestreo SMOTE para equilibrar las clases'
                           'dentro del pipeline de entrenamiento.',
                           style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                    html.H3('División de los datos',
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Se separaron en predictor y objetivo, con una división estratificada 60%% entrenamiento y 40%% test. '\
                           'Se utilizó la función train_test_split de sklearn para asegurar que la proporción de clases se mantuviera en ambas divisiones.',
                           style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                ]),
            ]),
            dcc.Tab(label='Selección del modelo', children=[
                html.Div([
                    html.H3('Modelo elegido', 
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Se utilizó Random Forest, una técnica de ensamblado basada en árboles de decisión.' \
                    'Este modelo fue seleccionado tras pruebas preliminares por su alto rendimiento predictivo e interpretabilidad',
                    style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                    html.H3('Justificación',
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Se buscó un modelo capaz de manejar datos de variables categoricas y numéricas, tolerante al desbalance de clases.',
                           style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                    html.H3('Configuración del modelo',
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.Code('''pipeline_rf = Pipeline([
                                ('smote', SMOTE(random_state=42)),
                                ('clf', RandomForestClassifier(
                                    n_estimators=200,
                                    max_depth=None,
                                    min_samples_split=2,
                                    random_state=42,
                                    class_weight='balanced'
                                ))
                            ])''',
                            style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                    html.H3('Ecuación del modelo',
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('El modelo Random Forest no tiene una ecuación explícita como un modelo lineal. '\
                           'Sin embargo, se puede describir su funcionamiento como una combinación de múltiples árboles de decisión. '\
                            'Cada árbol toma decisiones basadas en diferentes subconjuntos de datos y características, y el resultado final es la votación de todos los árboles.',
                            style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                ])
            ]),
            dcc.Tab(label='Evaluación del modelo', children=[
                html.Div([
                    html.H3('Entrenamiento', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('El modelo fue entrenado sobre el conjunto X_train, y_train. La ejecución completa tomó aproximadamente 163 segundos.',
                        style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                    html.H3('Métricas de evaluación',
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Recall: 0.8165 (Buena capacidad de detectar casos verdaderamente positivos)\n' \
                           'Precision: 0.9095 (Excelente discriminación general entre clases)\n'),
                    html.P('Proceso de entrenamiento, metricas, valuzacion usada, Aquí explicas los resultados de las evaluaciones o métricas.', 
                           style={'fontFamily': 'Lato', 'fontSize': '18px'})
                ])
            ]),
        ])
    ])

