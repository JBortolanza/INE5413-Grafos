from Grafo import *

arquivo = "ContemCicloEuleriano.net"
grafo = Grafo()
grafo.ler(arquivo)
vertice = "1"
print(grafo.GrafoEuleriano())