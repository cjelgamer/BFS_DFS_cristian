import numpy as np
import matplotlib.pyplot as plt

# Número de nodos en el grafo
num_nodes = 5

# Inicializar la matriz de adyacencia
adjacency_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

# Definir las aristas
edges = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 1)
]

# Llenar la matriz de adyacencia
for start, end in edges:
    adjacency_matrix[start][end] = 1

# Visualizar la matriz de adyacencia en forma de una tabla
fig, ax = plt.subplots(figsize=(6, 6))
ax.matshow(adjacency_matrix, cmap="Blues")

# Añadir etiquetas en la matriz para mejor legibilidad
for (i, j), val in np.ndenumerate(adjacency_matrix):
    ax.text(j, i, f'{val}', ha='center', va='center', color='black')

# Configuración de etiquetas en los ejes
ax.set_xticks(range(num_nodes))
ax.set_yticks(range(num_nodes))
ax.set_xticklabels(range(num_nodes))
ax.set_yticklabels(range(num_nodes))
plt.xlabel("Nodo destino")
plt.ylabel("Nodo origen")
plt.title("Matriz de Adyacencia del Grafo")

plt.show()
