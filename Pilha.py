class Pilha:
    def __init__(self, tam_max):
        self.elem = [None] * (tam_max + 1)
        self.topo = -1
        self.tam_max = tam_max

    def InicializaPilha(self):
        self.topo = -1

    def PilhaVazia(self):
        return self.topo == -1

    def PilhaCheia(self):
        return self.topo == self.tam_max

    def ElementoDoTopo(self):
        if not self.PilhaVazia():
            return self.elem[self.topo]

    def Empilha(self, x):
        if not self.PilhaCheia():
            self.topo += 1
            self.elem[self.topo] = x

    def Desempilha(self):
        if not self.PilhaVazia():
            x = self.elem[self.topo]
            self.topo -= 1
            if self.PilhaVazia():
                self.InicializaPilha()

# p = Pilha(3)
# print("Pilha vazia?", p.PilhaVazia())  
# p.Empilha(1)
# p.Empilha(20)
# p.Empilha(30)
# print("Pilha cheia?", p.PilhaCheia())  
# print("Elemento do topo:", p.ElementoDoTopo())
# p.Desempilha()
# p.Desempilha()
# p.Desempilha()
# print("Pilha cheia?", p.PilhaCheia())    
# print("Pilha vazia?", p.PilhaCheia())


#pilhas['p1'].insere_pilha(1)  # Insere na pilha p1
#print("Elemento do topo da pilha p1:", pilhas['p1'].elemento_topo())  # Saída: 1
