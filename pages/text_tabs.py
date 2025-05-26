# texto_tabs
from dash import html

def texto_tab1():
    return html.Div([
        html.H2('El Dengue en Colombia', style={'color': '#4B70F5', 'fontFamily': 'Poppins', 'marginBottom': '20px'}),

        html.Div([
            html.P(
                'El dengue es una enfermedad febril aguda de etiología viral, transmitida por vectores del género Aedes (A. aegypti y A. albopictus). '
                'Según la Organización Mundial de la Salud (OMS), esta patología representa una de las mayores cargas sanitarias en regiones tropicales ' 
                'y subtropicales, con un estimado de 390 millones de infecciones anuales a nivel global (OMS, 2023). Su espectro clínico varía desde formas '
                'asintomáticas hasta cuadros graves que requieren intervención médica urgente.',
                style={'fontFamily': 'Lato', 'fontSize': '20px'}
            ),
            html.P(
                'En Colombia, el dengue constituye un reto epidemiológico prioritario debido a su patrón endemo-epidémico y la amplia distribución del vector ' 
                'en el territorio nacional (73.3% según el INS, 2024). El Instituto Nacional de Salud (INS) reporta ciclos epidémicos cada 3 a 5 años, asociados'
                ' a factores climáticos y sociodemográficos. Desde 2013, el país ha fortalecido sus estrategias de vigilancia reforzada a través del '
                'Sistema Nacional de Vigilancia en Salud pública (SIVIGILA), que exige la notificación obligatoria de casos sospechosos y confirmados.',
                style={'fontFamily': 'Lato', 'fontSize': '20px'}
            )
        ], style={
            'border': '1px solid #ccc',
            'borderRadius': '8px',
            'padding': '15px',
            'marginBottom': '15px',
            'backgroundColor': '#f9f9f9',
            'boxShadow': '2px 2px 5px rgba(0, 0, 0, 0.1)'
        }),
    ])

def texto_tab2():
    return html.Div([
        html.H2('Contexto', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),

        html.Div([
            # Columna izquierda: logo
            html.Div([
                html.Img(
                    src='assets/sivigila.jpeg',  # Ruta del logo (debe estar en la carpeta /assets/)
                    style={'height': '120px', 'marginRight': '20px'}
                )
            ], style={'flex': '0 0 auto'}),

            # Columna derecha: texto
            html.Div([
                html.P(
                    'Los datos utilizados en este estudio fueron obtenidos del Sistema de Vigilancia en Salud Pública de Colombia (SIVIGILA), '
                    'el cual centraliza la notificación obligatoria de eventos de interés en salud pública, incluyendo el dengue y el dengue grave. '
                    'Esta plataforma permite acceder a reportes anuales de casos clasificados por variables clínicas, demográficas, geográficas y temporales.',
                    style={'fontFamily': 'Lato', 'fontSize': '20px'}
                ),
                html.P(
                    'Para este análisis se emplearon datos correspondientes al periodo comprendido entre los años 2013 y 2023, permitiendo capturar múltiples ciclos ' 
                    'epidémicos e identificar patrones estacionales y regionales en la ocurrencia de la enfermedad. '
                    'El enfoque se centró en la identificación de casos confirmados (por laboratorio o nexo epidemiológico) a partir de información asociada al paciente '
                    'y su entorno clínico.',
                    style={'fontFamily': 'Lato', 'fontSize': '20px'}
                )
            ], style={'flex': '1'})
        ], style={'display': 'flex', 'alignItems': 'flex-start', 'marginTop': '15px'})
    ])

def texto_tab3():
    return html.Div([
        html.H2('Problema', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
        html.P('*El dengue es una enfermedad de alta morbilidad y mortalidad, especialmente en poblaciones vulnerables. La identificación temprana y precisa de casos confirmados es crucial para la implementación de medidas de control y prevención efectivas. Sin embargo, la clasificación de casos puede ser complicada debido a la variabilidad clínica y la superposición con otras enfermedades transmitidas por vectores.', 
               style={'fontFamily': 'Lato', 'fontSize': '20px'}),
        html.P('*Este estudio busca abordar el problema de la clasificación de casos confirmados de dengue mediante el desarrollo de un modelo predictivo basado en aprendizaje automático. Se espera que este modelo no solo mejore la precisión en la identificación de casos, sino que también contribuya a optimizar los recursos destinados a la vigilancia epidemiológica y al manejo clínico de los pacientes.', 
               style={'fontFamily': 'Lato', 'fontSize': '20px'})
    ])

def texto_tab4():
    return html.Div([
        html.H2('Objetivos', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
        html.P('El objetivo principal de este estudio es desarrollar un modelo de aprendizaje automático para la clasificación precisa de casos confirmados de dengue, utilizando variables clínicas, demográficas y epidemiológicas extraídas de SIVIGILA. Dada la naturaleza de alto riesgo de los falsos negativos en este contexto, el modelo busca maximizar la sensibilidad (recall), es decir, la capacidad de identificar el mayor número posible de casos positivos, sin comprometer la estabilidad predictiva.', 
               style={'fontFamily': 'Lato', 'fontSize': '20px'}),
        html.P('Los objetivos específicos incluyen:', 
               style={'fontFamily': 'Lato', 'fontSize': '20px'}),
        html.Ul([
            html.Li('*Analizar la distribución temporal y geográfica de los casos de dengue.'),
            html.Li('*Identificar factores demográficos y clínicos asociados a la gravedad del dengue.')
        ], style={'fontFamily': 'Lato', 'fontSize': '20px'})
    ])

def texto_tab5():
    return html.Div([
        html.H2('Marco Teórico', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
        html.P('*El dengue es una enfermedad viral transmitida por mosquitos, con un ciclo de vida que incluye fases larvales y adultas. La transmisión ocurre principalmente a través de la picadura de mosquitos infectados del género Aedes, siendo A. aegypti el vector más relevante en áreas urbanas. La enfermedad presenta un espectro clínico que varía desde formas asintomáticas hasta cuadros graves, lo que dificulta su diagnóstico y manejo.', 
               style={'fontFamily': 'Lato', 'fontSize': '20px'}),
        html.P('*La clasificación de casos de dengue se basa en criterios clínicos, epidemiológicos y de laboratorio. Sin embargo, la variabilidad clínica y la superposición con otras enfermedades transmitidas por vectores complican esta tarea. En este contexto, el uso de modelos predictivos basados en aprendizaje automático se presenta como una herramienta prometedora para mejorar la precisión en la identificación de casos confirmados.', 
               style={'fontFamily': 'Lato', 'fontSize': '20px'})
    ])

def texto_tab8():
    return html.Div([
        html.H2('Conclusiones', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
        html.P('*El desarrollo de un modelo predictivo para la clasificación de casos confirmados de dengue representa un avance significativo en la vigilancia epidemiológica y el manejo clínico de esta enfermedad. La capacidad del modelo para maximizar la sensibilidad (recall) permitirá identificar un mayor número de casos positivos, contribuyendo a la implementación de medidas de control y prevención más efectivas.', 
               style={'fontFamily': 'Lato', 'fontSize': '20px'}),
        html.P('*Además, el análisis de la distribución temporal y geográfica de los casos, así como la identificación de factores demográficos y clínicos asociados a la gravedad del dengue, proporcionará información valiosa para la toma de decisiones en salud pública.', 
               style={'fontFamily': 'Lato', 'fontSize': '20px'})
    ])
