# ARCHIVO GENERAL

## Importar librerias
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from pages import metodos, resultados, text_tabs, callbacks

# DASH
# Diseño

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server
app.title = "Clasificación de Casos de Dengue"

# Layout general con estilo moderno
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    # Sidebar
    html.Div([
        html.H2("DENGUE APP", style={'textAlign': 'center', 'color': '#1f4e79'}),
        html.Hr(),
        dcc.Link('Introducción', href='/', className='nav-link'),
        dcc.Link('Contexto', href='/contexto', className='nav-link'),
        dcc.Link('Problema', href='/problema', className='nav-link'),
        dcc.Link('Objetivos', href='/objetivos', className='nav-link'),
        dcc.Link('Marco teórico', href='/teoria', className='nav-link'),
        dcc.Link('Metodología', href='/metodologia', className='nav-link'),
        dcc.Link('Resultados', href='/resultados', className='nav-link'),
        dcc.Link('Conclusiones', href='/conclusiones', className='nav-link'),
        html.Div([
            html.P("Creado por Daniela Acuña, Daniella Guerra & Tawny Torres", style={'fontSize': '12px'}),
            html.P("Datos: Portal Sivigila", style={'fontSize': '12px'})
        ], style={'padding-top': '20px', 'color': '#555'})
    ], className='sidebar'),

    # Contenido dinámico
    html.Div(id='page-content', className='content')
])

# Callback de navegación
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):

    if pathname == '/contexto':
        return text_tabs.texto_tab2()
    elif pathname == '/problema':
        return text_tabs.texto_tab3()
    elif pathname == '/objetivos':
        return text_tabs.texto_tab4()
    elif pathname == '/teoria':
        return text_tabs.texto_tab5()
    elif pathname == '/metodologia':
        return metodos.layout()
    elif pathname == '/resultados':
        return resultados.layout()
    elif pathname == '/conclusiones':
        return text_tabs.texto_tab8()
    else:
        return text_tabs.texto_tab1()

# Callbacks adicionales
callbacks.register(app)


if __name__ == '__main__':
    app.run(debug=True)
