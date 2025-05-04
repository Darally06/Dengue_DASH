import pandas as pd

def ajustar_variables(df):
    # Renombrar
    df.columns = [col.upper() for col in df.columns]

    # Ajustar la variable EDAD_AJUSTADA 
    # Conversion de la variable edad a numerica, reemplazar menores que 1, imputar NA con la MEDIADA
    df['EDAD_AJUSTADA']= pd.to_numeric(df['EDAD_AJUSTADA'], errors='coerce')
    df.loc[df["EDAD_AJUSTADA"] < 1, "EDAD_AJUSTADA"] = 1
    mediana_edad = df['EDAD_AJUSTADA'].median()
    df['EDAD_AJUSTADA'] = df['EDAD_AJUSTADA'].fillna(mediana_edad).astype('float64')

    # Convertir SEXO a variable numérica
    #df['SEXO'] = df['SEXO'].astype(str).str.strip()
    #df['SEXO_NUM'] = df['SEXO'].map({'F': 0, 'M': 1}).fillna(-1).astype('int64')

    # Convertir variables a numéricas
    columnas_a_convertir = ["GP_MIGRANT", "GP_POBICFB", "GP_GESTAN",
                            "AREA","SEMANA", "ANO","TIP_CAS",
                            "PAC_HOS", "CON_FIN", 
                            "CONFIRMADOS"]  
    for columna in columnas_a_convertir:
        df[columna] = pd.to_numeric(df[columna], errors='coerce').fillna(0).astype('int64')


    # Seleccionar columnas finales
    columnas_finales = [
        'EDAD_AJUSTADA', 'SEXO_NUM', 'TIP_SS', 
        'GP_MIGRANT', 'GP_POBICFB', 'GP_GESTAN',
        'AREA', 'PAIS_OCU', 'DPTO_OCU', 'MUN_OCU',
        'SEMANA', 'ANO', 
        'EVENTO', 'TIP_CAS', 
        'PAC_HOS', 'CON_FIN', 'CONFIRMADOS'
    ]
    df = df[columnas_finales]
    return df