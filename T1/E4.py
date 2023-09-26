from Grafo import *
import sys

def BellmanFord(grafo, s):
    # Inicializa as distancias com infinito e o predecessor como None
    dist = {v: float('inf') for v in grafo.vertices}
    pred = {v: None for v in grafo.vertices}
    dist[s] = 0

    # Relaxamento de arestas
    for _ in range(grafo.num_vertices - 1):
        for u, v, w in grafo.arestas:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u

        # Considerar o caso de v para u
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                pred[u] = v

    # Checar ciclos negativos
    for u, v, w in grafo.arestas:
        if dist[u] + w < dist[v]:
            raise ValueError("O grafo contém ciclos negativos")

    return pred, dist

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Esse progama recebe dois arguentos de entrada: nome do arquivo e vertice de inicio.")
        sys.exit(1)

    arquivo = sys.argv[1]
    origem = int(sys.argv[2])

    grafo = Grafo()
    grafo.ler(arquivo)
    pred, dist = BellmanFord(grafo, origem)

for v in grafo.vertices:
        if v != origem:
            caminho = []
            destino = v
            while destino is not None:
                caminho.insert(0, destino)
                destino = pred[destino]
            print(f"{v}:", ",".join(map(str, caminho)), f"; d={int(dist[v])}")