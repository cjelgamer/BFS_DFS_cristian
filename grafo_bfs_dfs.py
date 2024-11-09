import tkinter as tk
from tkinter import messagebox
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

# Grafo representado como lista de adyacencia
graph = {
    0: [1, 2],
    1: [2, 3],
    2: [3],
    3: [4],
    4: [1]
}

# Conjunto de aristas para el grafo
edges = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 1)
]

# Crear el grafo con networkx
G = nx.DiGraph()
G.add_edges_from(edges)

# Algoritmo BFS
def bfs(graph, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    
    return visited

# Algoritmo DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# Función para ejecutar el recorrido y mostrar el resultado
def execute_search(search_type):
    try:
        # Obtener el nodo de inicio desde el campo de entrada
        start_node = int(start_node_entry.get())
        if start_node not in graph:
            messagebox.showerror("Error", "El nodo de inicio no existe en el grafo.")
            return

        # Ejecutar el tipo de recorrido seleccionado
        if search_type == "BFS":
            result = bfs(graph, start_node)
            messagebox.showinfo("Resultado BFS", f"Orden de nodos visitados (BFS) desde {start_node}: {result}")
        elif search_type == "DFS":
            result = dfs(graph, start_node)
            messagebox.showinfo("Resultado DFS", f"Orden de nodos visitados (DFS) desde {start_node}: {result}")
        show_graph(result)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido para el nodo de inicio.")

# Función para mostrar el grafo y resaltar el recorrido
def show_graph(path):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightgray', font_size=15, font_weight='bold', edge_color='gray', arrows=True)
    
    # Resaltar el recorrido
    for i in range(len(path) - 1):
        nx.draw_networkx_nodes(G, pos, nodelist=[path[i]], node_color='skyblue')
        nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i + 1])], edge_color='blue', width=2.5)
    
    # Resaltar el último nodo del recorrido
    nx.draw_networkx_nodes(G, pos, nodelist=[path[-1]], node_color='skyblue')
    
    plt.title("Recorrido en el Grafo")
    plt.show()

# Crear interfaz gráfica
window = tk.Tk()
window.title("Recorridos en Grafos")
window.geometry("300x250")

# Etiqueta de instrucciones
label = tk.Label(window, text="Seleccione el tipo de recorrido y nodo de inicio:")
label.pack(pady=10)

# Campo de entrada para el nodo de inicio
start_node_label = tk.Label(window, text="Nodo de inicio:")
start_node_label.pack()
start_node_entry = tk.Entry(window)
start_node_entry.pack(pady=5)

# Botón para BFS
bfs_button = tk.Button(window, text="BFS (Breadth-First Search)", command=lambda: execute_search("BFS"))
bfs_button.pack(pady=5)

# Botón para DFS
dfs_button = tk.Button(window, text="DFS (Depth-First Search)", command=lambda: execute_search("DFS"))
dfs_button.pack(pady=5)

# Iniciar la interfaz gráfica
window.mainloop()
