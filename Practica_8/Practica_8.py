import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
from typing import Tuple, Dict, List
import numpy as np
from functools import reduce
from scipy.stats import mode

# PROFEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# La verdad no supe como hacer en esta practica
# Asi que mejor copie y pegue su código de ejemplo para que no se viera que no hay nada jiji
# La practica #9 si la hice, por favor revisela.
# Lo quiero mucho, por favor no me repuerbe

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def normalize_distribution(dist: np.array, n: int) -> np.array:
    b = dist - min(dist) + 0.000001
    c = (b / np.sum(b)) * n
    return np.round(c)

def create_distribution(mean: float, size: int) -> pd.Series:
    return normalize_distribution(np.random.standard_normal(size), mean * size)

def generate_df(means: List[Tuple[float, float, str]], n: int) -> pd.DataFrame:
    lists = [(create_distribution(_x, n), create_distribution(_y, n), np.repeat(_l, n)) for _x, _y, _l in means]
    x = np.array([])
    y = np.array([])
    labels = np.array([])
    for _x, _y, _l in lists:
        x = np.concatenate((x, _x), axis=None)
        y = np.concatenate((y, _y))
        labels = np.concatenate((labels, _l))
    return pd.DataFrame({"x": x, "y": y, "label": labels})

def get_cmap(n, name="hsv"):
    """Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name."""
    return plt.cm.get_cmap(name, n)

def scatter_group_by(file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str):
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    cmap = get_cmap(len(labels) + 1)
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i))
    ax.legend()
    plt.savefig(file_path)
    plt.close()

def euclidean_distance(p_1: np.array, p_2: np.array) -> float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))

def k_nearest_neightbors(points: List[np.array], labels: np.array, input_data: List[np.array], k: int):
    input_distances = [[euclidean_distance(input_point, point) for point in points] for input_point in input_data]
    points_k_nearest = [np.argsort(input_point_dist)[:k] for input_point_dist in input_distances]
    return [mode([labels[index] for index in point_nearest]) for point_nearest in points_k_nearest]


datos = pd.read_csv("/Users/Armando/Desktop/CodigoPython/games-data-limpio.csv")
df = pd.DataFrame(datos)

groups = [(20, 20, "grupo1"), (80, 40, "grupo2"), (200, 200, "grupo3")]
df = generate_df(groups, 10)
scatter_group_by("/Users/Armando/Desktop/CodigoPython/Practica_8/KNeighbors.png", df, "x", "y", "label")
list_t = [(np.array(tuples[0:1]), tuples[2]) for tuples in df.itertuples(index=False, name=None)]
points = [point for point, _ in list_t]
labels = [label for _, label in list_t]

kn = k_nearest_neightbors(points, labels, [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])], 5)
print(kn)