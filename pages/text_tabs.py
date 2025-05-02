# texto_tabs
from dash import html

def texto_tab1():
    return html.Div([
        html.H2('Introducción', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
        html.P('El dengue es una enfermedad viral transmitida por mosquitos que representa un importante problema de salud pública en Colombia.', 
               style={'fontFamily': 'Lato', 'fontSize': '18px'}),
        html.P('A lo largo de los últimos años, el país ha experimentado múltiples brotes que han afectado tanto zonas urbanas como rurales.', 
               style={'fontFamily': 'Lato', 'fontSize': '18px'}),
        html.H4('Objetivo del análisis', style={'color': '#3D3BF3', 'fontFamily': 'Open Sans', 'marginTop': '30px'}),
        html.P('El propósito de este dashboard es explorar, visualizar y entender la distribución y características de los casos de dengue en Colombia, '
               'utilizando datos históricos y demográficos para identificar patrones relevantes.', 
               style={'fontFamily': 'Lato', 'fontSize': '18px'}),
        html.p('Aquí se presenta una visión general del contexto de la problemática, el análisis realizado y los hallazgos encontrados.',
                'De manera resumida, indicar lo que se pretende lograr con el proyecto')
    ])

def texto_tab2():
    return """
    Contexto sobre el dengue en Colombia, incluyendo su epidemiología y factores de riesgo.
    Descripcion breve del contexto del proyecto, fuente de los datoa y nombre, variables de intetes y operacionalizacion
    """

def texto_tab3():
    return """
    Planteamiento del problema: la necesidad de un análisis exhaustivo de los datos de dengue en Colombia para mejorar la respuesta sanitaria.
    Describe la problematica abordada-
    Pregunta problema: ¿Cual es la pregunta que se quiere responder con el analisis?
    """

def texto_tab4():
    return """
    Objetivos y justificación del análisis: comprender la distribución de los casos de dengue y su relación con factores demográficos y geográficos.
    """

def texto_tab5():
    return """
    Marco teórico: conceptos clave sobre el dengue, su transmisión y factores de riesgo asociados.
    Resumen de conceptos teoricos (definiciones formales), referencias.
    """

def texto_tab8():
    return """
    Conclusiones generales, hallazgos y recomendaciones finales.
    """
