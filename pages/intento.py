import plotly.io as pio
import requests

url = "https://raw.githubusercontent.com/Darally06/Resultados_json/refs/heads/main/jsons/fig_dptos.json"
r = requests.get(url)
print(r.status_code)
print(r.text[:200])  # muestra un resumen del contenido
fig = pio.from_json(r.text)
fig.show()