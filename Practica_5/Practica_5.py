import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols


datos = pd.read_csv("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
df = pd.DataFrame(datos)

df.boxplot("Score", by="Anio", figsize=(15,9))
plt.xticks(rotation=45)
plt.title("Scores dados por año", fontsize=16)
plt.xlabel("Años", fontsize=13)
plt.ylabel("Score", fontsize=13)
plt.savefig('/Users/Armando/Desktop/CodigoPython/Practica_5/score_anio.jpeg', bbox_inches='tight')# , bbox_inches='tight')
plt.show()

mod = ols("Score ~ Anio", data=df).fit()
aov_table = sm.stats.anova_lm(mod, typ=2)
# print(aov_table)
if aov_table["PR(>F)"][0] < 0.005:
    print("hay diferencias")

    print(aov_table)
    # Prueba tukey
    # imprimir los resultados
else:
    print("No hay diferencias")

'''

# Teorema de limite central sobre el Score

# Primero calculamos los valores necesarios
media = df['Score'].mean()
desvet = np.std(df['Score'])
n = len(df)

# print("Media: ", media)
# print("Desviación estandar: ", desvet)
# print("Tamaño: ", n)

z = stats.norm.ppf(1-0.05/2)
# print("z = ", z)

# Error
E = z*desvet/np.sqrt(n)
# print("El error es: ", E)

# print("El intervalo de confianza es: ", media-E, " < miu < ", media+E)

nn = ((z*desvet)/E)**2
# print(nn)

# Grados de libertad
gl = n - 1
# print("Grados de libertad: ", gl)

Chili = stats.chi2.ppf(0.975, gl)
Chils = stats.chi2.ppf(0.025, gl)
# print(Chili, Chils)

# Varianza
v = desvet**2
liminf = (gl*v)/Chili
limsup = (gl*v)/Chils


# Prueba de hipotesis

# Establecemos media de la población y la desviación estandar
mean, std = 40, desvet

# Calculamos el error estandar
se = std / np.sqrt(n)

# Estadistica Z
Z = (media - mean)/se

print("La estadistica Z es {}".format(Z))

# Valor P
P = 2 * stats.norm.sf(abs(Z))
print("El valor p es {}".format(P))

'''
