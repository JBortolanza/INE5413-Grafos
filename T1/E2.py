from Grafo import *
from collections import deque
import sys

def buscaLargura(grafo, origem):
    if origem not in grafo.vertices:
        return "Origem não existe no grafo"
    
    niveis = {}  # Dicionário para armazenar os níveis dos vértices
    fila = deque()  # Fila para realizar a busca em largura
    
    # Inicializa a busca a partir da origem
    fila.append(origem)
    niveis[origem] = 0
    
    resultado = {}  # Dicionário para armazenar os vértices por nível
    
    while fila:
        vertice_atual = fila.popleft()
        
        if niveis[vertice_atual] not in resultado:
            resultado[niveis[vertice_atual]] = [vertice_atual]
        else:
            resultado[niveis[vertice_atual]].append(vertice_atual)
        
        for vizinho in grafo.vizinhos(vertice_atual):
            if vizinho not in niveis:
                fila.append(vizinho)
                niveis[vizinho] = niveis[vertice_atual] + 1
    
    return resultado

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Esse progama recebe dois arguentos de entrada: nome do arquivo e vertice de inicio.")
        sys.exit(1)

    arquivo = sys.argv[1]
    origem = int(sys.argv[2])

    grafo = Grafo()
    grafo.ler(arquivo)
    resultado =buscaLargura(grafo, origem)

    for key, values in resultado.items():
        values_str = ', '.join(map(str, values))
        print(f"{key}: {values_str}")

