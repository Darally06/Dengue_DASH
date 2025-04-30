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
    ])

def texto_tab2():
    return """
    Explicación detallada de la pestaña 2, comparaciones de años, etc.
    """

def texto_tab3():
    return """
    Información sobre la distribución espacial del dengue en Colombia.
    """

def texto_tab4():
    return """
    Análisis de tendencias temporales de casos reportados.
    """

def texto_tab5():
    return """
    Distribución por sexo, edad y área de residencia.
    """

def texto_tab8():
    return """
    Conclusiones generales, hallazgos y recomendaciones finales.
    """
