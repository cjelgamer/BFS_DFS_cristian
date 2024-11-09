import matplotlib.pyplot as plt

# Número de nodos en el grafo
num_nodes = 5

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

# Crear la lista de adyacencia
adjacency_list = {i: [] for i in range(num_nodes)}
for start, end in edges:
    adjacency_list[start].append(end)

# Visualizar la lista de adyacencia como una tabla
fig, ax = plt.subplots(figsize=(6, num_nodes))

# Convertir la lista de adyacencia a un texto formateado para mostrar en la figura
adjacency_text = "\n".join([f"{node}: {', '.join(map(str, neighbors))}" for node, neighbors in adjacency_list.items()])

# Mostrar el texto en la gráfica
ax.text(0.5, 0.5, adjacency_text, ha='center', va='center', fontsize=12, family='monospace')
ax.axis('off')  # Ocultar ejes

plt.title("Lista de Adyacencia del Grafo")
plt.show()
