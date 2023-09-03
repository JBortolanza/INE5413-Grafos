class Grafo:
    def __init__(self):
        self.vertices = {}  # Dicionario para guardar vertices e rotulos
        self.arestas = []  # Lista para armazenar as arestas e pesos
        self.num_vertices = 0
        self.num_arestas = 0

    def qtdVertices(self):
        return self.num_vertices

    def qtdArestas(self):
        return self.num_arestas
    
    def grau(self, v): 
        if v in self.vertices:
            grau = 0
            for item in self.arestas:
                if item[0] == v or item[1] == v:
                    grau += 1
            return grau
        else:
            return "Esse vertice nao existe no grafo" 
    
    def rotulo(self, v):
        if v in self.vertices:
            return self.vertices[v]
        else:
            return "Esse vertice nao existe no grafo" 
    
    def vizinhos(self, v):
        if v in self.vertices:
            vizinhos = []
            for item in self.arestas:
                if item[0] == v:
                    vizinhos.append(item[1])
                if item[1] == v:
                    vizinhos.append(item[0])
            return vizinhos
        else:
            return "Esse vertice nao existe no grafo" 
    
    def haAresta(self, u, v):
        if v in self.vertices and u in self.vertices:
            for item in self.arestas:
                if (item[0] == v and item[1] == u) or (item[0] == u and item[1] == v):
                    return True
            return False
        else:
            return "Esse(s) vertice(s) nao existe no grafo" 
        
    def peso(self, u, v):
        if v in self.vertices and u in self.vertices:
            for item in self.arestas:
                if (item[0] == v and item[1] == u) or (item[0] == u and item[1] == v):
                    return item[2]
            return float('inf')
        else:
            return "Esse(s) vertice(s) nao existe no grafo" 
    
    def ler(self, arquivo):
        with open(arquivo, 'r') as file:
            lines = file.readlines()

            lendo_vertices = True
            for line in lines:
                line = line.strip()

                if line.startswith('*vertices'):
                    lendo_vertices = True
                    continue
                elif line.startswith('*edges'):
                    lendo_vertices = False
                    continue

                if lendo_vertices:
                    if line != '':
                        partes = line.split()
                        indice = int(partes[0])  # Índice do vértice
                        rotulo = ' '.join(partes[1:]).strip('"')  # Rótulo do vértice
                        self.vertices[indice] = rotulo
                        self.num_vertices += 1
                else:
                    if line != '':
                        partes = line.split()
                        u = int(partes[0])  # Índice do vértice u
                        v = int(partes[1])  # Índice do vértice v
                        peso = float(partes[2])
                        self.arestas.append((u, v, peso))
                        self.num_arestas += 1