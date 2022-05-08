from statistics import mean
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List

#Funcion que nos ayuda con el formato de la impresion del .csv
def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

#Función para realizar analisis de las diferentes plataformas
def df_plataforma(file_name:str):
    df = pd.read_csv(file_name)
    df_plataforma = df.groupby(["Plataforma"]).agg({"Nombre": ["count"], "Score": ["max", "min",
    "mean", "median", "mad"], "Score_Jugadores": ["max", "min", "mean", "median", "mad"], "Criticos":
    ["sum", "mean", "median"], "Usuarios": ["sum", "mean", "median"]})
    # df_plataforma = df_plataforma.reset_index()
    df_plataforma = df_plataforma[["Nombre", "Score", "Score_Jugadores", "Criticos", "Usuarios"]].reset_index()
    # print_tabulate(df_plataforma)
    df_plataforma.columns = ['Plataforma', 'Cantidad_Juegos', 'Score_Max', 'Score_Min', 'Score_Prom', 'Score_Mediana', 'Score_Mad',
    'Score_Jugadores_Max', 'Score_Jugadores_Min', 'Score_Jugadores_Prom', 'Score_Jugadores_Mediana', 'Score_Jugadores_Mad',
    'Criticos_Sum', 'Criticos_Prom', 'Criticos_Mediana', 'Usuarios_Sum', 'Usuarios_Prom', 'Usuarios_Mediana']
    print_tabulate(df_plataforma.head())
    df_plataforma.to_csv('/Users/Armando/Desktop/CodigoPython/Practica_3/df_plataforma.csv', index=True)

# Función para realizar analisis de que tantos juegos comparten el mismo score
def df_frecuencia_score(file_name:str):
    df = pd.read_csv(file_name)
    df_frecuencia_score = df.groupby(["Score"]).agg({"Nombre": ["count"]})
    # df_frecuencia_score = df_frecuencia_score.reset_index()
    df_frecuencia_score = df_frecuencia_score[["Nombre"]].reset_index()
    df_frecuencia_score.columns = ['Score', 'Cantidad_Juegos']
    print_tabulate(df_frecuencia_score.head())
    df_frecuencia_score.to_csv('/Users/Armando/Desktop/CodigoPython/Practica_3/df_frecuencia_score.csv', index=True)


# Función para realizar analisis de que tantos juegos comparten el mismo score dado por jugadores
def df_frecuencia_score_jugadores(file_name:str):
    df = pd.read_csv(file_name)
    df_frecuencia_score_jugadores = df.groupby(["Score_Jugadores"]).agg({"Nombre": ["count"]})
    # df_frecuencia_score_jugadores = df_frecuencia_score_jugadores.reset_index()
    df_frecuencia_score_jugadores = df_frecuencia_score_jugadores[["Nombre"]].reset_index()
    df_frecuencia_score_jugadores.columns = ['Score_Jugadores', 'Cantidad_Juegos']
    print_tabulate(df_frecuencia_score_jugadores.head())
    df_frecuencia_score_jugadores.to_csv('/Users/Armando/Desktop/CodigoPython/Practica_3/df_frecuencia_score_jugadores.csv', index=True)


# Analisis de la columna Desarrollador
def df_desarrollador(file_name:str):
    df = pd.read_csv(file_name)
    df_desarrollador = df.groupby(["Desarrollador"]).agg({"Nombre": ["count"], "Score": ["max", "min",
    "mean", "median", "mad"], "Score_Jugadores": ["max", "min", "mean", "median", "mad"]})
    # df_desarrollador = df_desarrollador.reset_index()
    df_desarrollador = df_desarrollador[["Nombre", "Score", "Score_Jugadores"]].reset_index()
    df_desarrollador.columns = ['Desarrollador', 'Cantidad_Juegos', 'Score_Max', 'Score_Min', 'Score_Prom', 'Score_Mediana', 'Score_Mad',
    'Score_Jugadores_Max', 'Score_Jugadores_Min', 'Score_Jugadores_Prom', 'Score_Jugadores_Mediana', 'Score_Jugadores_Mad']
    print_tabulate(df_desarrollador.head())
    df_desarrollador.to_csv('/Users/Armando/Desktop/CodigoPython/Practica_3/df_desarrollador.csv', index=True)

# Analisis tomando como referencia la columna Jugadores
def df_jugadores(file_name:str):
    df = pd.read_csv(file_name)
    df_jugadores = df.groupby(["Jugadores"]).agg({"Nombre": ["count"]})
    # df_jugadores = df_jugadores.reset_index()
    df_jugadores = df_jugadores[["Nombre"]].reset_index()
    df_jugadores.columns = ['Jugadores', 'Cantidad_Juegos']
    print_tabulate(df_jugadores.head())
    df_jugadores.to_csv('/Users/Armando/Desktop/CodigoPython/Practica_3/df_jugadores.csv', index=True)

# Analisis de tomando como referencia la columna Anios
def df_anios(file_name:str):
    df = pd.read_csv(file_name)
    df_anios = df.groupby(["Anio"]).agg({"Nombre": ["count"], "Score": ["max", "min", "mean", "median",
    "mad"], "Score_Jugadores": ["max", "min", "mean", "median", "mad"], "Criticos": ["sum", "mean",
    "median"], "Usuarios": ["sum", "mean", "median"]})
    # df_anios = df_anios.reset_index()
    df_anios = df_anios[["Nombre", "Score", "Score_Jugadores", "Criticos", "Usuarios"]].reset_index()
    df_anios.columns = ['Anio', 'Cantidad_Juegos', 'Score_Max', 'Score_Min', 'Score_Prom', 'Score_Mediana', 'Score_Mad',
    'Score_Jugadores_Max', 'Score_Jugadores_Min', 'Score_Jugadores_Prom', 'Score_Jugadores_Mediana', 'Score_Jugadores_Mad',
    'Criticos_Sum', 'Criticos_Prom', 'Criticos_Mediana', 'Usuarios_Sum', 'Usuarios_Prom', 'Usuarios_Mediana']
    print_tabulate(df_anios.head())
    df_anios.to_csv('/Users/Armando/Desktop/CodigoPython/Practica_3/df_anios.csv', index=True)

# Analisis de tomando como referencia la columna Nombre_Dia
def df_nombre_dia(file_name:str):
    df = pd.read_csv(file_name)
    df_nombre_dia = df.groupby(["Nombre_Dia"]).agg({"Nombre": ["count"], "Score": ["max", "min", "mean", "median",
    "mad"], "Score_Jugadores": ["max", "min", "mean", "median", "mad"], "Criticos": ["sum", "mean",
    "median"], "Usuarios": ["sum", "mean", "median"]})
    # df_nombre_dia = df_nombre_dia.reset_index()
    df_nombre_dia = df_nombre_dia[["Nombre", "Score", "Score_Jugadores", "Criticos", "Usuarios"]].reset_index()
    df_nombre_dia.columns = ['Nombre_Dia', 'Cantidad_Juegos', 'Score_Max', 'Score_Min', 'Score_Prom', 'Score_Mediana', 'Score_Mad',
    'Score_Jugadores_Max', 'Score_Jugadores_Min', 'Score_Jugadores_Prom', 'Score_Jugadores_Mediana', 'Score_Jugadores_Mad',
    'Criticos_Sum', 'Criticos_Prom', 'Criticos_Mediana', 'Usuarios_Sum', 'Usuarios_Prom', 'Usuarios_Mediana']
    print_tabulate(df_nombre_dia.head())
    df_nombre_dia.to_csv('/Users/Armando/Desktop/CodigoPython/Practica_3/df_nombre_dia.csv', index=True)

# Analisis de tomando como referencia la columna Mes
def df_mes(file_name:str):
    df = pd.read_csv(file_name)
    df_mes = df.groupby(["Mes"]).agg({"Nombre": ["count"], "Score": ["max", "min", "mean", "median",
    "mad"], "Score_Jugadores": ["max", "min", "mean", "median", "mad"], "Criticos": ["sum", "mean",
    "median"], "Usuarios": ["sum", "mean", "median"]})
    # df_mes = df_mes.reset_index()
    df_mes = df_mes[["Nombre", "Score", "Score_Jugadores", "Criticos", "Usuarios"]].reset_index()
    df_mes.columns = ['Mes', 'Cantidad_Juegos', 'Score_Max', 'Score_Min', 'Score_Prom', 'Score_Mediana', 'Score_Mad',
    'Score_Jugadores_Max', 'Score_Jugadores_Min', 'Score_Jugadores_Prom', 'Score_Jugadores_Mediana', 'Score_Jugadores_Mad',
    'Criticos_Sum', 'Criticos_Prom', 'Criticos_Mediana', 'Usuarios_Sum', 'Usuarios_Prom', 'Usuarios_Mediana']
    print_tabulate(df_mes.head())
    df_mes.to_csv('/Users/Armando/Desktop/CodigoPython/Practica_3/df_mes.csv', index=True)

# Llamadas a las funciones previamente tecleadas
#df_plataforma("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
#df_frecuencia_score("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
#df_frecuencia_score_jugadores("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
#df_desarrollador("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
#df_jugadores("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
#df_anios("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
df_nombre_dia("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
#df_mes("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")