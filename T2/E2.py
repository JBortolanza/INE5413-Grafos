from Grafo import *

def DFS_topologica(grafo):

    # Funcao declarada dentro para poder compartilhar variaveis sem necessidade de passagem
    def DFS_Visit_OT(vertice):
        visitados[vertice] = True
        nonlocal tempo
        tempo += 1
        temposI[vertice] = tempo

        for vizinho in grafo.vizinhosM(vertice):
            if visitados[vizinho] == False:
                DFS_Visit_OT(vizinho)

        tempo += 1
        temposF[vertice] = tempo
        ord.insert(0, vertice)
    # Fim funcao

    visitados = {v: False for v in grafo.vertices}
    temposI = {v: float('inf') for v in grafo.vertices}
    temposF = {v: float('inf') for v in grafo.vertices}
    tempo = 0
    ord = []

    for vertice in grafo.vertices:
        if visitados[vertice] == False:
            DFS_Visit_OT(vertice)

    return ord

if __name__ == '__main__':
    grafo = Grafo()
    grafo.ler('manha.net')
    vertices_ordenados = DFS_topologica(grafo)
    vp = [grafo.vertices[v] for v in vertices_ordenados]
    print(' → '.join(vp))