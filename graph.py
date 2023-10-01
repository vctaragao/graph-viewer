import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import numpy as np

adjacency_matrix = pd.read_csv('Lista de materias - CCO.csv', header=None).values
G = nx.DiGraph(adjacency_matrix)

in_degrees = dict(G.in_degree())
out_degrees = dict(G.out_degree())

print("In-degrees:", in_degrees)
print("Out-degrees:", out_degrees)

nx.draw(G, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black', arrows=True)
plt.show()

