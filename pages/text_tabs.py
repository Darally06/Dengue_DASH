# texto_tabs
from dash import html

def texto_tab1():
    return html.Div([
        html.H2('Introducción', style={'color': '#4B70F5', 'fontFamily': 'Poppins'}),
        html.P('El dengue es una enfermedad viral aguda transmitida por mosquitos infectados, ' \
        'considerada una de las principales amenazas para la salud pública en regiones tropicales'\
        'y subtropicales, afectando a millones de personas anualmente (OMS, 2023).',
        style={'fontFamily': 'Lato', 'fontSize': '18px'}),
        html.P('En Colombia, su prevención y control son prioritarios debido a la presencia del vector' \
        ' y las condiciones climáticas favorables para su propagación. ' \
        'Sin embargo, no todos los casos reportados han sido confirmados mediante pruebas diagnosticas',
        style={'fontFamily': 'Lato', 'fontSize': '18px'}),
        html.P('Los resultados del análisis propuesto pueden contribuir a mejorar la estimación de casos futuros, ' \
        'optimizar la toma de decisiones en salud pública y fortalecer las estrategias de prevención',
        style={'fontFamily': 'Lato', 'fontSize': '18px'}),
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
