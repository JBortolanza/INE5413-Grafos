from Grafo import *


def DFS(grafo):

    # Funcao declarada dentro para poder compartilhar variaveis sem necessidade de passagem
    def DFS_Visit(vertice):
        visitados[vertice] = True
        nonlocal tempo
        tempo += 1
        temposI[vertice] = tempo

        for vizinho in grafo.vizinhosM(vertice):
            if visitados[vizinho] == False:
                arvores[vizinho] = vertice
                DFS_Visit(vizinho)

        tempo += 1
        temposF[vertice] = tempo
    # Fim funcao

    visitados = {v: False for v in grafo.vertices}
    temposI = {v: float('inf') for v in grafo.vertices}
    temposF = {v: float('inf') for v in grafo.vertices}
    arvores = {v: None for v in grafo.vertices}
    tempo = 0

    for vertice in grafo.vertices:
        if visitados[vertice] == False:
            DFS_Visit(vertice)

# Exemplo de uso:
if __name__ == '__main__':
    grafo = Grafo()
    grafo.ler('fln_pequena.net')  # Substitua 'exemplo.txt' pelo nome do arquivo com o seu grafo

    sccs = encontrarSCC(grafo)

    for scc in sccs:
        print(scc)