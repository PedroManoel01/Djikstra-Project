class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1].append([v, peso])


    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

arquivo = open('roadNet-TX.txt','r')
g = Grafo(1379917)
for line in arquivo:
    line = line.split(" ")
    print(line[0])