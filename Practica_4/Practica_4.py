import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# PROFE, si las graficas no cargan a la primera entonces pruebe recargando la página
# A mi me funcionó la mayoria de las veces.
# Tuve también que instalar Kaleido usando el siguiente comando: pip install -U kaleido

sns.set_style("whitegrid")
sns.set(rc={'figure.figsize':(10,6)})

# Variables que almacenando los distintos datasets creados en la practica 3
df = pd.read_csv("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
df_plataforma = pd.read_csv("/Users/Armando/Desktop/CodigoPython/df_plataforma.csv")
df_mes = pd.read_csv("/Users/Armando/Desktop/CodigoPython/df_mes.csv")
df_nombre_dia = pd.read_csv("/Users/Armando/Desktop/CodigoPython/df_nombre_dia.csv")
df_anios = pd.read_csv("/Users/Armando/Desktop/CodigoPython/df_anios.csv")

# Histograma de valores promedio de Score
promedio_score = df['Score'].mean()
fig = px.histogram(df, x='Score', title='Valor promedio: '+str(promedio_score), opacity = 0.6)
fig.update_layout(yaxis_title="Cantidad de juegos")
fig.add_shape(
            type="line",
            x0=df['Score'].mean(),
            y0=0,
            x1=df['Score'].mean(),
            y1=700,
            line=dict(
                color="darkblue",
                width=4
            ),
    )
fig.show()
fig.write_image('/Users/Armando/Desktop/CodigoPython/Practica_4/promedio_score.jpeg')

# Histograma de valores promedio de Score dados por jugadores
promedio_score_jugadores = df[df['Score_Jugadores'] != 0.0]['Score_Jugadores'].mean()
fig = px.histogram(df[df['Score_Jugadores'] != 0.0], x="Score_Jugadores", title = 'Valor promedio: '+str(promedio_score_jugadores), opacity = 0.6)
fig.update_layout(yaxis_title="Cantidad de juegos")
fig.add_shape(
            type="line",
            x0=df[df['Score_Jugadores'] != 0.0]['Score_Jugadores'].mean(),
            y0=0,
            x1=df[df['Score_Jugadores'] != 0.0]['Score_Jugadores'].mean(),
            y1=700,
            line=dict(
                color="darkblue",
                width=4
            ),
    )
fig.show()
fig.write_image('/Users/Armando/Desktop/CodigoPython/Practica_4/promedio_score_jugadores.jpeg')

# Hacer la grafica de barras de df_plataforma.csv
fig = px.bar(df_plataforma, x='Plataforma', y=('Score_Prom'), color='Score_Jugadores_Prom').update_xaxes(categoryorder="total descending")
fig.show()
fig.write_image('/Users/Armando/Desktop/CodigoPython/Practica_4/plataforma_score_prom.jpeg')

# Distribución por mes de lanzamiento de los Score
fig = px.scatter(df, x='Score', y='Mes', color='Plataforma', hover_name='Nombre')
fig.show()
fig.write_image('/Users/Armando/Desktop/CodigoPython/Practica_4/promedio_score_mes.jpeg')

# Ploteo de un boxplot tomando como base los Scores
plt.figure(figsize=(15,9))
sns.boxplot(x='Plataforma', y='Score', data=df)
plt.xticks(rotation=45)
plt.savefig('/Users/Armando/Desktop/CodigoPython/Practica_4/boxplot_plataforma_score_prom.jpeg')
plt.show()

# Grafica de barras sobre la cantidad de juegos lanzada por plataforma
fig = px.bar(df_plataforma, x='Plataforma', y='Cantidad_Juegos').update_xaxes(categoryorder="total descending")
fig.show()
fig.write_image('/Users/Armando/Desktop/CodigoPython/Practica_4/cant_juegos_plataforma.jpeg')

# Grafica de barras sobre la cantidad de juegos lanzada por mes
fig = px.bar(df_mes, x='Mes', y='Cantidad_Juegos')
fig.show()
fig.write_image('/Users/Armando/Desktop/CodigoPython/Practica_4/cant_juegos_mes.jpeg')

# Grafica de barras sobre la cantidad promedio de Score de juegos por mes
fig = px.bar(df_mes, x='Mes', y='Score_Prom')
fig.show()
fig.write_image('/Users/Armando/Desktop/CodigoPython/Practica_4/score_juegos_prom_mes.jpeg')

# Grafica de barras sobre la cantidad promedio de juegos salidos por dia
fig = px.bar(df_nombre_dia, x='Nombre_Dia', y='Cantidad_Juegos',
             category_orders = {
                                    'Nombre_Dia': ['Dom','Lun','Mar','Mie','Jue','Vie','Sab']
                                },
                                labels = {
                                    'Nombre_Dia': 'Dia de la semana'
                                })
fig.show()
fig.write_image('/Users/Armando/Desktop/CodigoPython/Practica_4/cant_juegos_prom_dia.jpeg')

# Grafica de barras sobre el Score promedio de juegos ordenado por dia
fig = px.bar(df_nombre_dia, x='Nombre_Dia', y='Score_Prom')
fig.show()
fig.write_image('/Users/Armando/Desktop/CodigoPython/Practica_4/score_prom_dia.jpeg')

# Grafica de barras sobre el Score por jugadores promedio de juegos ordenado por dia
fig = px.bar(df_nombre_dia, x='Nombre_Dia', y='Score_Jugadores_Prom')
fig.show()
fig.write_image('/Users/Armando/Desktop/CodigoPython/Practica_4/score_jugadores_prom_dia.jpeg')

# Grafica de barras sobre la cantidad de juegos lanzada por año
fig = px.bar(df_anios, x='Anio', y='Cantidad_Juegos')
fig.show()
fig.write_image('/Users/Armando/Desktop/CodigoPython/Practica_4/juegos_anio.jpeg')

# Grafica de barras sobre la cantidad promedio de Score de juegos lanzada por año
fig = px.bar(df_anios, x='Anio', y='Score_Prom')
fig.show()
fig.write_image('/Users/Armando/Desktop/CodigoPython/Practica_4/score_prom_anio.jpeg')

# Grafica de barras sobre la cantidad promedio de Score dada por jugadores lanzada por año
fig = px.bar(df_anios, x='Anio', y='Score_Jugadores_Prom')
fig.show()
fig.write_image('/Users/Armando/Desktop/CodigoPython/Practica_4/score_jugadores_prom_anio.jpeg')