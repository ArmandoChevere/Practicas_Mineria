import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from tabulate import tabulate
import numbers
import statsmodels.api as sm
# import numpy as np
# from sklearn import linear_model

# regr = linear_model.LinearRegression()
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
    print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[pd.DataFrame.mean(df[y]) for _ in fixed_x.items()], color='green')
    plt.plot(df_anio[x],[ coef.values[1] * x + coef.values[0] for _, x in fixed_x.items()], color='red')
    plt.xticks(rotation=90)
    plt.savefig(f'/Users/Armando/Desktop/CodigoPython/Practica_6/lr_{y}_{x}.png')
    plt.close()

df_anio = df.groupby("Anio").aggregate(Score_Prom=pd.NamedAgg(column="Score", aggfunc=pd.DataFrame.mean))
# df_anio["Score_Prom"] = df_anio["Score_Prom"]**10
df_anio.reset_index(inplace=True)
print_tabulate(df_anio)

linear_regression(df_anio, "Anio", "Score_Prom")


'''

regr = linear_model.LinearRegression()
datos = pd.read_csv("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
df = pd.DataFrame(datos)
x=df["Anio"]
y=df["Score"]

X=x[:,np.newaxis]
print(X)
print(regr.fit(X,y))
print(regr.coef_)
m=regr.coef_[0]
b=regr.intercept_
y_p=m*X+b
print("Modelo de regresión lineal:")
print("y={0}*x+1{1}".format(m, b))
print("Algunas predicciones:")
print(regr.predict(X)[0:5])
print("El valor de r al cuadrado: ", r2_score(y, y_p))
score_prom = df['Score'].mean()
score_prom = [score_prom] * 17944

# Ploteo de la regresión lineal
plt.scatter(x, y, color="blue")
plt.plot(x, y_p, color="red")
plt.plot(x, score_prom, color="green")
plt.title("Regresión lineal", fontsize=16)
plt.xlabel("Años", fontsize=13)
plt.ylabel("Score", fontsize=13)
plt.savefig('/Users/Armando/Desktop/CodigoPython/Practica_6/regresion_lineal_anios_score.jpeg')
plt.show()

'''

