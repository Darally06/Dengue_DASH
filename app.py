# ARCHIVO GENERAL

## Importar librerias
import psycopg2
import dash
from dash import dcc, html
import pandas as pd
from dash.dependencies import Input, Output
from pages import metodos, resultados, text_tabs, change_df, callbacks

## Conexion a la base de datos
conexion = psycopg2.connect(
    host="localhost",
    database="data_dengue",
    user="postgres",
    password="Darally",
    port="5432"
)
#Holis
query = "SELECT * FROM base_dengue_raw;"
df = pd.read_sql(query, conexion)
conexion.close()

df = change_df.ajustar_variables(df)
df.to_csv("data/dengue.csv", index=False)

# DASH
# Diseño
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Clasificación de Casos de Dengue"

# Layout general
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # Sidebar
    html.Div([
        html.H2("DENGUE APP", style={'textAlign': 'center', 'color': '#4B70F5', 'fontFamily': 'Poppins'}),
        html.Hr(),
        html.Div(id='sidebar-links'),  # Generado dinámicamente
        html.Div([
            html.P("Creado por Daniela Acuña, Daniella Guerra & Tawny Torres", style={'fontSize': '14px'}),
            html.P("Datos: Portal Sivigila", style={'fontSize': '14px'})
        ], style={'fontFamily': 'Lato', 'fontSize': '18px'},)
    ], className='sidebar'),

    # Contenido dinámico
    html.Div(id='page-content', className='content')
])

# Callback de contenido principal
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
        return metodos.layout(df)
    elif pathname == '/resultados':
        return resultados.layout(df)
    elif pathname == '/conclusiones':
        return text_tabs.texto_tab8()
    else:
        return text_tabs.texto_tab1()

# Callback para resaltar el enlace activo
@app.callback(
    Output('sidebar-links', 'children'),
    Input('url', 'pathname')
)
def update_sidebar(pathname):
    links = [
        ('/', 'Introducción'),
        ('/contexto', 'Contexto'),
        ('/problema', 'Problema'),
        ('/objetivos', 'Objetivos'),
        ('/teoria', 'Marco teórico'),
        ('/metodologia', 'Metodología'),
        ('/resultados', 'Resultados'),
        ('/conclusiones', 'Conclusiones'),
    ]

    return [
        dcc.Link(text, href=link, className='nav-link active' if pathname == link else 'nav-link')
        for link, text in links
    ]

# Callbacks adicionales
callbacks.register(app, df)

if __name__ == '__main__':
    app.run(debug=True)
