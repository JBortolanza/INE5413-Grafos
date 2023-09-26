from Grafo import *
import sys

def FloydWarshall(grafo):
    num_vertices = grafo.qtdVertices()
    # Cria matriz de adjacencias com distancia incial infinita
    distancias = [[float('inf') for _ in range(num_vertices)] for _ in range(num_vertices)]

    # Coloca distancia de um vertice para si proprio em 0
    for i in range(num_vertices):
        distancias[i][i] = 0

    # Coloca os pesos das arestas do grafo na matriz
    for u, v, peso in grafo.arestas:
        distancias[u-1][v-1] = peso
        distancias[v-1][u-1] = peso  # Adiciona a aresta no sentido oposto para lidar com grafo nao dirigido
    print(distancias)

    # Algoritmo de Floyd-Warshall
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]

    return distancias

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Esse progama recebe um arguento de entrada: nome do arquivo.")
        sys.exit(1)

    arquivo = sys.argv[1]

    grafo = Grafo()
    grafo.ler(arquivo)
    resultado = FloydWarshall(grafo)

    for i, linha in enumerate(resultado):
        linha_formatada = ','.join(str(int(d)) for d in linha)
        print(f"{i+1}:{linha_formatada}")