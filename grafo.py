import matplotlib.pyplot as plt
import networkx as nx

# Definir el conjunto de aristas
edges = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 1)
]

# Crear un grafo dirigido
G = nx.DiGraph()
G.add_edges_from(edges)

# Dibujar el grafo
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_size=700, node_color='lightblue', font_size=15, font_weight='bold', edge_color='gray', arrows=True)
plt.title("Grafo dirigido")
plt.show()
