# ARCHIVO GENERAL

## Importar librerias
import dash
from dash import dcc, html
import pandas as pd 
import psycopg2
from pages import metodos, resultados, text_tabs, change_df

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
app.layout = html.Div([
    html.H1("CLASIFICACIÓN DE CASOS DE DENGUE", style={'textAlign': 'center'}),
    
    dcc.Tabs([
        dcc.Tab(label='Introducción', children=[
            text_tabs.texto_tab1()
        ]),
        dcc.Tab(label='Contexto', children=[
            text_tabs.texto_tab2()
        ]),
        dcc.Tab(label='Planteamiento del problema', children=[
            text_tabs.texto_tab3()
        ]),
        dcc.Tab(label='Objetivos y justificación', children=[
            text_tabs.texto_tab4()
        ]),
        dcc.Tab(label='Marco teórico', children=[
            html.Div("Contenido Tab 5")
        ]),
        dcc.Tab(label='Metodología', children = metodos.layout(df)),
        dcc.Tab(label='Resultados y análisis', children = resultados.layout(df)),
        dcc.Tab(label='Conclusiones', children = [
            text_tabs.texto_tab8()
        ]),
    ])
])

if __name__ == '__main__':
    app.run(debug=True)