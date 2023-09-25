from Grafo import *
from collections import deque
import sys

def Hierholzer(grafo):

    def remove_aresta(u, v):
        for i, (x, y, peso) in enumerate(grafo.arestas):
            if (x == u and y == v) or (x == v and y == u):
                grafo.arestas.pop(i)
                break

    def visitar_vertice(v):
        nonlocal ciclo
        while grafo.vizinhos(v):
            proximo_vizinho = grafo.vizinhos(v)[0] 
            remove_aresta(v, proximo_vizinho) 
            visitar_vertice(proximo_vizinho)
        ciclo.append(str(v))

    if not grafo.GrafoEuleriano(): # Caso o grafo nao seja euleriano ja retorna 0;
        return 0
    ciclo = []
    visitar_vertice(1)
    return ciclo

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Esse progama recebe um arguento de entrada: nome do arquivo.")
        sys.exit(1)

    arquivo = sys.argv[1]

    grafo = Grafo()
    grafo.ler(arquivo)
    resultado = Hierholzer(grafo)
    if resultado == 0:
        print(0)
    else:
        print(1)
        print(", ".join(resultado))