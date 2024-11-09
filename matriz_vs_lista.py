import numpy as np
import sys
import time
from collections import deque
import tkinter as tk
import random

# Definir un grafo dirigido grande con 1000 nodos y 2000 aristas aleatorias
num_nodes = 1000
edges = [(random.randint(0, num_nodes - 1), random.randint(0, num_nodes - 1)) for _ in range(2000)]

# Función para crear la matriz de adyacencia
def create_adjacency_matrix(edges, num_nodes):
    adjacency_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
    for start, end in edges:
        adjacency_matrix[start][end] = 1
    return adjacency_matrix

# Función para crear la lista de adyacencia
def create_adjacency_list(edges, num_nodes):
    adjacency_list = {i: [] for i in range(num_nodes)}
    for start, end in edges:
        adjacency_list[start].append(end)
    return adjacency_list

# Implementación de BFS en matriz de adyacencia
def bfs_matrix(matrix, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in range(len(matrix[node])):
                if matrix[node][neighbor] == 1 and neighbor not in visited:
                    queue.append(neighbor)
    return visited

# Implementación de DFS en matriz de adyacencia
def dfs_matrix(matrix, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in range(len(matrix[start])):
        if matrix[start][neighbor] == 1 and neighbor not in visited:
            dfs_matrix(matrix, neighbor, visited)
    return visited

# Implementación de BFS en lista de adyacencia
def bfs_list(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    return visited

# Implementación de DFS en lista de adyacencia
def dfs_list(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_list(graph, neighbor, visited)
    return visited

# Medición de tiempo y espacio para BFS y DFS en ambas representaciones
def measure_bfs_dfs_time_space(matrix, graph_list):
    # BFS con Lista de Adyacencia
    start_time = time.time()
    bfs_list_result = bfs_list(graph_list, 0)
    bfs_list_time = time.time() - start_time
    bfs_list_space = sys.getsizeof(graph_list) + sys.getsizeof(bfs_list_result)

    # DFS con Lista de Adyacencia
    start_time = time.time()
    dfs_list_result = dfs_list(graph_list, 0)
    dfs_list_time = time.time() - start_time
    dfs_list_space = sys.getsizeof(graph_list) + sys.getsizeof(dfs_list_result)

    # BFS con Matriz de Adyacencia
    start_time = time.time()
    bfs_matrix_result = bfs_matrix(matrix, 0)
    bfs_matrix_time = time.time() - start_time
    bfs_matrix_space = sys.getsizeof(matrix) + sys.getsizeof(bfs_matrix_result)

    # DFS con Matriz de Adyacencia
    start_time = time.time()
    dfs_matrix_result = dfs_matrix(matrix, 0)
    dfs_matrix_time = time.time() - start_time
    dfs_matrix_space = sys.getsizeof(matrix) + sys.getsizeof(dfs_matrix_result)

    return (bfs_list_time, dfs_list_time, bfs_list_space, dfs_list_space, bfs_list_result, dfs_list_result,
            bfs_matrix_time, dfs_matrix_time, bfs_matrix_space, dfs_matrix_space, bfs_matrix_result, dfs_matrix_result)

# Crear la matriz y la lista de adyacencia
adjacency_matrix = create_adjacency_matrix(edges, num_nodes)
adjacency_list = create_adjacency_list(edges, num_nodes)

# Función para iniciar el análisis
def start_analysis():
    (bfs_list_time, dfs_list_time, bfs_list_space, dfs_list_space, bfs_list_result, dfs_list_result,
     bfs_matrix_time, dfs_matrix_time, bfs_matrix_space, dfs_matrix_space, bfs_matrix_result, dfs_matrix_result) = measure_bfs_dfs_time_space(adjacency_matrix, adjacency_list)

    # Actualizar etiquetas de resultados
    bfs_list_label.config(text=f"BFS Lista - Tiempo: {bfs_list_time:.6f} s, Espacio: {bfs_list_space} bytes")
    dfs_list_label.config(text=f"DFS Lista - Tiempo: {dfs_list_time:.6f} s, Espacio: {dfs_list_space} bytes")
    bfs_matrix_label.config(text=f"BFS Matriz - Tiempo: {bfs_matrix_time:.6f} s, Espacio: {bfs_matrix_space} bytes")
    dfs_matrix_label.config(text=f"DFS Matriz - Tiempo: {dfs_matrix_time:.6f} s, Espacio: {dfs_matrix_space} bytes")
    
    # Mostrar los recorridos con puntos suspensivos si son muy largos
    bfs_list_result_label.config(text=f"Recorrido BFS Lista: {str(bfs_list_result[:50]) + '...'}")
    dfs_list_result_label.config(text=f"Recorrido DFS Lista: {str(dfs_list_result[:50]) + '...'}")
    bfs_matrix_result_label.config(text=f"Recorrido BFS Matriz: {str(bfs_matrix_result[:50]) + '...'}")
    dfs_matrix_result_label.config(text=f"Recorrido DFS Matriz: {str(dfs_matrix_result[:50]) + '...'}")

# Función para mostrar la matriz de adyacencia en una ventana nueva
def show_adjacency_matrix():
    matrix_window = tk.Toplevel(window)
    matrix_window.title("Matriz de Adyacencia")
    matrix_text = tk.Text(matrix_window, height=30, width=80)
    matrix_text.pack()
    matrix_text.insert(tk.END, str(adjacency_matrix))

    # Guardar la matriz completa en un archivo de texto
    np.savetxt("matriz_adyacencia_completa.txt", adjacency_matrix, fmt='%d')
    print("Matriz de adyacencia guardada en 'matriz_adyacencia_completa.txt'")

# Función para mostrar la lista de adyacencia en una ventana nueva
def show_adjacency_list():
    list_window = tk.Toplevel(window)
    list_window.title("Lista de Adyacencia")
    list_text = tk.Text(list_window, height=30, width=80)
    list_text.pack()
    list_text.insert(tk.END, str(adjacency_list))

# Interfaz Gráfica
window = tk.Tk()
window.title("Análisis de Complejidad")
window.geometry("800x1000")

# Botón para comenzar el análisis
start_button = tk.Button(window, text="Comenzar Análisis", command=start_analysis)
start_button.pack(pady=10)

bfs_list_label = tk.Label(window, text="BFS Lista - Tiempo y Espacio")
bfs_list_label.pack(pady=5)

dfs_list_label = tk.Label(window, text="DFS Lista - Tiempo y Espacio")
dfs_list_label.pack(pady=5)

bfs_matrix_label = tk.Label(window, text="BFS Matriz - Tiempo y Espacio")
bfs_matrix_label.pack(pady=5)

dfs_matrix_label = tk.Label(window, text="DFS Matriz - Tiempo y Espacio")
dfs_matrix_label.pack(pady=5)

bfs_list_result_label = tk.Label(window, text="Recorrido BFS Lista:")
bfs_list_result_label.pack(pady=10)

dfs_list_result_label = tk.Label(window, text="Recorrido DFS Lista:")
dfs_list_result_label.pack(pady=10)

bfs_matrix_result_label = tk.Label(window, text="Recorrido BFS Matriz:")
bfs_matrix_result_label.pack(pady=10)

dfs_matrix_result_label = tk.Label(window, text="Recorrido DFS Matriz:")
dfs_matrix_result_label.pack(pady=10)

# Botones para mostrar la matriz y lista de adyacencia en ventanas separadas
matrix_button = tk.Button(window, text="Mostrar Matriz de Adyacencia", command=show_adjacency_matrix)
matrix_button.pack(pady=10)

list_button = tk.Button(window, text="Mostrar Lista de Adyacencia", command=show_adjacency_list)
list_button.pack(pady=10)

# Mostrar las aristas generadas
edges_label = tk.Label(window, text="Aristas generadas:")
edges_label.pack(pady=10)
edges_text = tk.Text(window, height=10, width=80)
edges_text.pack()
edges_text.insert(tk.END, str(edges))

window.mainloop()
