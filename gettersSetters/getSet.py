"""Crie uma classe e insira nela, no mínimo, dois atributos, 
os quais devem ter um método acessor (get) e um método modificador (set) para cada. 
Defina um objeto para cada atributo e elabore um construtor para criar alguma regra.

A atividade pode ser realizada em qualquer linguagem de programação ou apenas utilizando algoritmos."""


class Produto:
    def __init__(self, nome, preco, percentual):
        self.nome = nome
        self.preco = preco
        self.percentual = percentual

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if(valor > 0):
            self._preco = valor
        else:
            self._preco = 0

    def desconto(self):
        self.preco = self.preco - (self.preco * (self.percentual/100))
        return self.preco

    @property
    def percentual(self):
        return self._percentual

    @percentual.setter
    def percentual(self, porcent):
        if(0 <= porcent <= 100):
            self._percentual = porcent
        else:
            self._percentual = 0 


p1 = Produto("Smart Phone", 2500, 15)
p2 = Produto("camisa", 78, 20) 
p3 = Produto("meia", -10, 15)
p4 = Produto("relógia", 1237, 120)

print(p1.preco, p1.desconto())
print(p2.preco, p2.desconto())
print(p3.preco, p3.desconto())
print(p4.preco, p4.desconto())

# Resultado no terninal:
# 2500 2125.0
# 78 62.4
# 0 0
# 1237 1237.0