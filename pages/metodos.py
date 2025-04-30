from dash import html, dcc

def layout(df):
    return html.Div([
        dcc.Tabs([
            dcc.Tab(label='Definición del problema', children=[
                html.Div([
                    html.H3('Metodología General', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Aquí describes la metodología general del proyecto.', style={'fontFamily': 'Lato', 'fontSize': '18px'})
                ])
            ]),
            dcc.Tab(label='Preparación de Datos', children=[
                html.Div([
                    html.H3('Preparación de Datos', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Aquí describes cómo procesaste los datos, limpieza, normalización, etc.', style={'fontFamily': 'Lato', 'fontSize': '18px'})
                ])
            ]),
            dcc.Tab(label='Selección del modelo', children=[
                html.Div([
                    html.H3('Modelado', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Aquí explicas qué modelos o análisis usaste, decisiones tomadas, etc.', style={'fontFamily': 'Lato', 'fontSize': '18px'})
                ])
            ]),
            dcc.Tab(label='Evaluación del modelo', children=[
                html.Div([
                    html.H3('Evaluación', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
                    html.P('Aquí explicas los resultados de las evaluaciones o métricas.', style={'fontFamily': 'Lato', 'fontSize': '18px'})
                ])
            ]),
        ]),
    ])

