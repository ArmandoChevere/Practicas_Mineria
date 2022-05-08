import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

datos = pd.read_csv("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
df = pd.DataFrame(datos)

x = df["Anio"].values
y = df["Score"].values

# info = df[["Anio", "Score"]].as_matrix()
# print(info)

X = np.array(list(zip(x,y)))
print(X)

kmeans = KMeans(n_clusters=3)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_

colors = ["m.", "r.", "c.", "y.", "b."]

for i in range(len(X)):
    print("Coordena: ", X[i], "Label: ", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

plt.scatter(centroids[:,0], centroids[:,1], marker = 'x', s=150, linewidths=5, zorder=10)
plt.xlabel("Años", fontsize=14)
plt.ylabel("Score", fontsize=14)
plt.title("Clustering", fontsize=18)
plt.savefig('/Users/Armando/Desktop/CodigoPython/Practica_9/clustering.png')
plt.show()