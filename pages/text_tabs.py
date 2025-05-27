# texto_tabs
from dash import html

def texto_tab1():
    return html.Div([
        html.H2('El Dengue en Colombia', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '36px', 'marginBottom': '20px'}),

        html.Div([
            # Columna izquierda: imagen o logo
            html.Div([
                html.Img(
                    src='assets/Aedes_aegypti_Adult_Feeding.jpg', 
                    style={'height': '500px', 'marginRight': '30px'}
                )
            ], style={'flex': '0 0 auto'}),

            # Columna derecha: texto
            html.Div([
                html.P('El dengue es una enfermedad febril aguda de etiología viral, transmitida por vectores del género Aedes (A. aegypti y A. albopictus).',
                    style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                html.P('Esta patología representa una de las mayores cargas sanitarias en regiones tropicales y subtropicales, con un estimado de 390 millones de infecciones anuales a nivel global (OMS, 2023).',
                    style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                html.P('Su espectro clínico varía desde formas asintomáticas hasta cuadros graves que requieren intervención médica urgente.',
                    style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                html.P('En Colombia, el dengue constituye un reto epidemiológico prioritario debido a su patrón endemo-epidémico y la amplia distribución del vector en el territorio nacional (73.3% según el INS, 2024). ', 
                    style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                html.P('Desde 2013, el país ha fortalecido sus estrategias de vigilancia reforzada a través del Sistema Nacional de Vigilancia en Salud pública (SIVIGILA), que exige la notificación obligatoria de casos sospechosos y confirmados.', 
                    style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
            ], style={'flex': '1'})
        ], style={
            'display': 'flex',
            'alignItems': 'flex-start',
            'borderRadius': '8px',
            'padding': '15px',
            'marginBottom': '15px',
            'backgroundColor': '#f9f9f9',
            'boxShadow': '2px 2px 5px rgba(0, 0, 0, 0.1)'
        }),
    ])


def texto_tab2():
    return html.Div([
        html.H2('Contexto', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'font-size': '36px'}),

        html.Div([
            # Columna izquierda: logo
            html.Div([
                html.Img(
                    src='assets/sivigila.jpeg',  # Ruta del logo (debe estar en la carpeta /assets/)
                    style={'height': '300px', 'marginRight': '30px'}
                )
            ], style={'flex': '0 0 auto'}),

            # Columna derecha: texto
            html.Div([
                html.P(
                    'Los datos utilizados en este estudio fueron obtenidos del Sistema de Vigilancia en Salud Pública de Colombia (SIVIGILA), '
                    'el cual centraliza la notificación obligatoria de eventos de interés en salud pública, incluyendo el dengue y el dengue grave. '
                    'Esta plataforma permite acceder a reportes anuales de casos clasificados por variables clínicas, demográficas, geográficas y temporales.',
                    style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                html.P(
                    'Para este análisis se emplearon datos correspondientes al periodo comprendido entre los años 2013 y 2023, permitiendo capturar múltiples ciclos ' 
                    'epidémicos e identificar patrones estacionales y regionales en la ocurrencia de la enfermedad. '
                    'El enfoque se centró en la identificación de casos confirmados (por laboratorio o nexo epidemiológico) a partir de información asociada al paciente '
                    'y su entorno clínico.',
                    style={'fontFamily': 'Century Gothic', 'fontSize': '24px'})
            ], style={'flex': '1'})
        ], style={'display': 'flex', 'alignItems': 'flex-start', 'marginTop': '15px'})
    ])


def texto_tab3():
    return html.Div([
        html.H2('Problema', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'font-size': '36px'}),

        html.Div([
            html.Img(
                src='assets/clinic.jpg',  # Cambia esto al nombre real de tu archivo
                style={
                    'height': '500px',
                    'width': '500px',
                    'marginRight': '30px',
                    'objectFit': 'contain'
                }
            ),
            html.Div([
                html.P('El dengue constituye una enfermedad viral con altos niveles de morbilidad y mortalidad, particularmente en poblaciones vulnerables.',
                       style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                html.P('La detección temprana y precisa de los casos confirmados es fundamental para la implementación eficaz de estrategias de control y prevención.',
                       style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                html.P('Sin embargo, su clasificación puede verse dificultada por la variabilidad clínica y la coexistencia con otras enfermedades transmitidas por vectores.',
                       style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),

                html.P('En este estudio, se aborda dicho reto mediante el desarrollo de un modelo predictivo basado en aprendizaje automático, diseñado para mejorar la precisión en la clasificación de casos confirmados de dengue. ',
                       style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                html.P('Se espera que este modelo no solo optimice la detección de casos positivos, sino que también contribuya a una asignación más eficiente de los recursos destinados a la vigilancia epidemiológica y al manejo clínico de los pacientes.',
                       style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
            ])
        ], style={'display': 'flex', 'alignItems': 'flex-start', 'marginTop': '10px'})
    ])


def texto_tab4():
    return html.Div([
        html.H2('Objetivos', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'marginBottom': '20px', 'fontSize': '36px'}),

        html.Div([
            # Objetivo General con ícono a la izquierda
            html.Div([
                html.H4('Objetivo General', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'marginBottom': '15px', 'fontSize': '30px'}),
                html.P('Desarrollar un modelo de aprendizaje automático capaz de clasificar de forma precisa los casos confirmados de dengue.',
                       style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
                
                html.P('Dada la criticidad de minimizar los falsos negativos en contextos de salud pública, el modelo busca maximizar la sensibilidad (recall), ' 
                    'es decir, identificar la mayor cantidad posible de casos positivos sin comprometer la estabilidad predictiva.',
                    style={'fontFamily': 'Century Gothic', 'fontSize': '24px'})
            ]),

            # Objetivos específicos como lista con estilo
            html.Div([
                html.H4('Objetivos Específicos', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'marginBottom': '10px', 'fontSize': '30px'}),
                html.Ul([
                    html.Li('🔹Analizar la distribución temporal y geográfica de los casos de dengue en Colombia entre 2013 y 2023.'),
                    html.Li('🔹Identificar variables clínicas y demográficas asociadas a la gravedad de la enfermedad y su confirmación diagnóstica.')
                ], style={'fontFamily': 'Century Gothic', 'fontSize': '24px','listStyleType': 'none','paddingLeft': '0px','lineHeight': '1.8'})
            ])
        ], style={
            'backgroundColor': '#f9f9f9',
            'padding': '25px',
            'borderRadius': '10px',
            'boxShadow': '2px 2px 8px rgba(0, 0, 0, 0.1)'
        })
    ])


def texto_tab5():
    return html.Div([
        html.H2('Marco Teórico', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '36px'}),
        
        html.Div([
            html.P('El dengue es una enfermedad viral transmitida por mosquitos del género Aedes, particularmente Aedes aegypti, vector predominante en zonas urbanas. ',
                   style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
            html.P('Su ciclo de vida incluye fases larvarias y adultas, y su transmisión ocurre mediante la picadura de hembras infectadas. ',
                   style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
            html.P('La enfermedad presenta un amplio espectro clínico, desde infecciones asintomáticas hasta cuadros graves, lo que complica tanto su diagnóstico como su abordaje terapéutico.',
                style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
            html.P('La clasificación de los casos de dengue se basa en criterios clínicos, epidemiológicos y de laboratorio. No obstante, la variabilidad en las manifestaciones clínicas, '
                'así como la superposición con otras enfermedades transmitidas por vectores, dificulta su identificación precisa. ',
                style={'fontFamily': 'Century Gothic', 'fontSize': '24px'}),
            html.P('En este escenario, el uso de modelos predictivos basados en aprendizaje automático se presenta como una herramienta innovadora y prometedora para mejorar la precisión en la detección de casos confirmados, '
                'aportando valor a la vigilancia epidemiológica automatizada.',
                style={'fontFamily': 'Century Gothic', 'fontSize': '24px'})
        ], style={
            'backgroundColor': '#f9f9f9',
            'padding': '25px',
            'borderRadius': '10px',
            'boxShadow': '2px 2px 8px rgba(0, 0, 0, 0.1)'
        }),
    ])


def texto_tab8():
    return html.Div([
        html.H2('Conclusiones', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'fontSize': '24px'}),
        html.Ul([
                html.Li('🔹 SD-GBClassifier es una herramienta robusta, sensible e interpretable para la predicción de casos confirmados'),
                html.Li('🔹 Este modelo puede aplicarse como un filtro para priorizar alertas clínicas'),
                html.Li('🔹 Se recomienda incorporar más datos y explorar enfoques basados en modelos temporales.'),
            ], style={'fontFamily': 'Century Gothic', 'fontSize': '24px','listStyleType': 'none','paddingLeft': '0px','lineHeight': '1.8'})
        ])
