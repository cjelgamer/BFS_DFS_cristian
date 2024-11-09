# Análisis de Grafos con BFS y DFS

Este repositorio contiene código en Python para analizar grafos mediante recorridos de búsqueda en anchura (BFS) y en profundidad (DFS). Se representan los grafos usando listas y matrices de adyacencia, y se miden los tiempos y el uso de memoria de cada método para comparar su eficiencia en distintas estructuras de datos.

## Estructura de Archivos

- **grafo.py**: Define un grafo con 5 nodos y sus aristas. También incluye la generación de su lista y matriz de adyacencia.
- **lista.py**: Contiene la representación del grafo usando una lista de adyacencia.
- **matriz.py**: Contiene la representación del grafo usando una matriz de adyacencia.
- **grafo_bfs_dfs.py**: Implementa los algoritmos de BFS y DFS para recorrer el grafo. Este archivo se utiliza en el segundo ejercicio para realizar los recorridos y observar sus resultados.
- **matriz_vs_lista.py**: Genera tanto la matriz como la lista de adyacencia y permite utilizar cada una con los algoritmos de recorrido para comparar el tiempo y el uso de memoria. Este archivo es fundamental para el tercer ejercicio, donde se analiza el rendimiento de cada estructura.
- **matriz_adyacencia_completa.txt**: Archivo generado automáticamente al ejecutar el tercer ejercicio. Contiene la representación completa de la matriz de adyacencia del grafo.

## Ejercicios

1. **Definición del Grafo**: En grafo.py se define el grafo con sus conexiones, y se generan sus representaciones en lista (lista.py) y en matriz (matriz.py).
   
2. **Recorridos con BFS y DFS**: El archivo grafo_bfs_dfs.py implementa los algoritmos BFS y DFS, y permite realizar los recorridos en el grafo. Aquí se observa el funcionamiento y el orden de visita de cada nodo.

3. **Análisis de Complejidad**: Usando el archivo matriz_vs_lista.py, se genera la lista y la matriz de adyacencia del grafo y se aplican los algoritmos de recorrido. Se mide el tiempo de ejecución y el consumo de memoria de cada estructura, comparando su rendimiento en distintas configuraciones.

## Instrucciones

1. Clona este repositorio en tu máquina local.
   
   ```bash
   git clone <https://github.com/cjelgamer/BFS_DFS_cristian.git>
