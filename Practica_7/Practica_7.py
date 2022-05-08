import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
from tabulate import tabulate
from statsmodels.stats.outliers_influence import summary_table
from typing import Tuple, Dict
import numpy as np

datos = pd.read_csv("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
df = pd.DataFrame(datos)

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def transform_variable(df: pd.DataFrame, x:str)->pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x] # type: pd.Series
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def linear_regression(df: pd.DataFrame, x:str, y: str)->None:
    fixed_x = transform_variable(df, x)
    model= sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    # print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[pd.DataFrame.mean(df[y]) for _ in fixed_x.items()], color='green')
    plt.plot(df_anio[x],[ coef.values[1] * x + coef.values[0] for _, x in fixed_x.items()], color='red')
    plt.xticks(rotation=90)
    plt.savefig('/Users/Armando/Desktop/CodigoPython/Practica_7/lr_Score_Anio.png')
    plt.close()

df_anio = df.groupby("Anio").aggregate(Score_Prom=pd.NamedAgg(column="Score", aggfunc=pd.DataFrame.mean))
# df_anio["Score_Prom"] = df_anio["Score_Prom"]**10
df_anio.reset_index(inplace=True)
print_tabulate(df_anio)

linear_regression(df_anio, "Anio", "Score_Prom")

# Empezamos a pronosticar

df_anio["MA"] = df_anio["Score_Prom"].rolling(window=3).mean().shift(1)
df_anio["Anio"] = df_anio["Anio"].astype(int)
df_anio["Score_Prom"] = df_anio["Score_Prom"].astype(float)
df_anio["MA"] = df_anio["MA"].astype(float)

# Agregar más registros al dataset
for n in range(3):
    df_anio.loc[len(df_anio)]=[int(df_anio.iloc[len(df_anio)-1][0]) + 1, 0, 0]

df_anio["MA"] = df_anio["Score_Prom"].rolling(window=3).mean().shift(1)
df_anio["Anio"] = df_anio["Anio"].astype(int)
df_anio["Score_Prom"] = df_anio["Score_Prom"].astype(float)
df_anio["MA"] = df_anio["MA"].astype(float)

print_tabulate(df_anio)

plt.figure(figsize=(15,9))
plt.plot(df_anio['Anio'][:-3], df_anio['Score_Prom'][:-3], '-o', color='blue', label='data de los promedios')
plt.plot(df_anio['Anio'], df_anio['MA'], '-o', color='red', label='forecast')
plt.xlabel("Años", fontsize=14)
plt.ylabel("Score_Prom", fontsize=14)
plt.title("Forecast", fontsize=18)
plt.legend(loc='best')
plt.savefig('/Users/Armando/Desktop/CodigoPython/Practica_7/forecasting_Score_Anio.png')
plt.show()



'''

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def transform_variable(df: pd.DataFrame, x:str)->pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x] # type: pd.Series
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def linear_regression(df: pd.DataFrame, x:str, y: str)->Dict[str, float]:
    fixed_x = transform_variable(df, x)
    model= sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    bands = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]
    print_tabulate(pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0])
    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    r_2_t = pd.read_html(model.summary().tables[0].as_html(),header=None,index_col=None)[0]
    return {'m': coef.values[1], 'b': coef.values[0], 'r2': r_2_t.values[0][3], 'r2_adj': r_2_t.values[1][3], 'low_band': bands['[0.025'][0], 'hi_band': bands['0.975]'][0]}

def plt_lr(df: pd.DataFrame, x:str, y: str, m: float, b: float, r2: float, r2_adj: float, low_band: float, hi_band: float, colors: Tuple[str,str]):
    fixed_x = transform_variable(df, x)
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[ m * x + b for _, x in fixed_x.items()], color=colors[0])
    plt.fill_between(df[x],
                     [ m * x  + low_band for _, x in fixed_x.items()],
                     [ m * x + hi_band for _, x in fixed_x.items()], alpha=0.2, color=colors[1])


datos = pd.read_csv("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
df = pd.DataFrame(datos)

df_anio = df.groupby("Anio").aggregate(Score_Prom=pd.NamedAgg(column="Score", aggfunc=pd.DataFrame.mean))
# df_anio["Score_Prom"] = df_anio["Score_Prom"]**10
df_anio.reset_index(inplace=True)
print_tabulate(df_anio)

a = linear_regression(df_anio, "Anio", "Score_Prom")
plt_lr(df=df_anio, x="Anio", y="Score_Prom", colors=('red', 'orange'), **a)

plt.xticks(rotation=90)
plt.savefig('/Users/Armando/Desktop/CodigoPython/Practica_7/lr_Score_Anio.png')
plt.close()

'''

