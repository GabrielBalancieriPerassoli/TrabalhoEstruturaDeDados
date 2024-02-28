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

