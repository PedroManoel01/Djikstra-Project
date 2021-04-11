class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafo[u].append([v, peso])
    
    def djikstra(self,origem,destino):
        distancia = [999999999999999] * self.vertices

        distancia[origem] = 0
        distancia_no = {origem:0}

        while distancia_no:
            no_origem = min(distancia_no, key= lambda x : distancia_no[x])
            del distancia_no[no_origem]
            for no in self.grafo[no_origem]:
                no_vizinho = no[0] 
                distancia_vizinho = no[1]

                if distancia[no_vizinho] > (distancia[no_origem] + distancia_vizinho):
                     distancia[no_vizinho] = distancia[no_origem] + distancia_vizinho
                     distancia_no[no_vizinho] = distancia[no_vizinho]
        print("a distancia entre",str(origem),"e",str(destino),"eh",str(distancia[destino]))

def procurarOrigem(origem, arquivo):
    for line in arquivo:
        if line[0] == origem or line[1] == origem:
            return True
        else:
            return False

def procurarDestino(destino, arquivo):
    for line in arquivo:
        if line[0] == destino or line[1] == destino:
            return True
        else:
            return False

arquivo = open('roadNet-TX.txt','r')
g = Grafo(1393383)
for line in arquivo:
    line = line[:-1]
    line = line.split("\t")
    if int(line[0]) > int(line[1]):
        peso = int(line[0]) - int(line[1])
    else:
        peso = int(line[1]) - int(line[0])
    g.adiciona_aresta(int(line[0]),int(line[1]),peso)

origem = int(input("insira o vértice de origem:"))
destino = int(input("insira o vértice de destino:"))

resultOrigem = procurarOrigem(origem, arquivo)
resultDestino = procurarDestino(destino, arquivo)

if resultOrigem == False or resultDestino == False:
    print('Vértice de origem ou destino inválida.')
else: 
    g.djikstra(origem,destino)


    
