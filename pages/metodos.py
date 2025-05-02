from dash import html, dcc

def layout(df):
    return html.Div([
        dcc.Tabs([
            dcc.Tab(label='Definición del problema', children=[
                html.Div([
                    html.H3('Problema', 
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Predecir si un caso registrado en la base de datos debe ser',
                            html.B('confirmado'),
                            'como positivo para dengue o no, utilizando técnicas de aprendizaje automático',
                            style={'fontFamily': 'Lato', 'fontSize': '18px'}),
                    html.H3('Variable objetivo',
                            style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('La variable objetivo es',
                            html.Code('CONFIRMADOS'),', que indica si un caso fue finalmente confirmado como positivo' \
                            'por laboratorio o por nexo epidemiológico',
                            html.Code('True'), 'o no',
                            html.Code('False'), 'para dengue.'\
                            'Este es un problema de clasificación binaria, con clases desbalanceadas.')  
                ])
            ]),
            dcc.Tab(label='Preparación de Datos', children=[
                html.Div([
                    html.H3('Preparación de Datos', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Aquí describes cómo procesaste los datos, limpieza, normalización, etc., division del data set en entrenamiento', 
                           style={'fontFamily': 'Lato', 'fontSize': '18px'})
                ])
            ]),
            dcc.Tab(label='Selección del modelo', children=[
                html.Div([
                    html.H3('Modelado', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Modelo selccionado, justificacion, ecuacion matematica, Aquí explicas qué modelos o análisis usaste, decisiones tomadas, etc.', 
                           style={'fontFamily': 'Lato', 'fontSize': '18px'})
                ])
            ]),
            dcc.Tab(label='Evaluación del modelo', children=[
                html.Div([
                    html.H3('Evaluación', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Proceso de entrenamiento, metricas, valuzacion usada, Aquí explicas los resultados de las evaluaciones o métricas.', 
                           style={'fontFamily': 'Lato', 'fontSize': '18px'})
                ])
            ]),
        ]),
    ])

