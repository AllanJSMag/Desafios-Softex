#Criando um TAD para calcular números complexos

"""Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python.
O método deve:

- calcular três números complexos;
- realizar todas as operações básicas;
- e imprimir as propriedades real e img do números."""


class NumerosComplexos:
    def __init__(self, num1:complex, num2:complex):
        self.num1 = num1 
        self.num2 = num2

    def soma(self):
        soma = self.num1 + self.num2
        print("O resultado da soma é = " + str(soma))
        print("A parte real é: " + str(soma.real))
        print("A parte imaginária é: " + str(soma.imag))

    def subtraicao(self):
        sub = self.num1 - self.num2
        print("O resultado da subtração é = " + str(sub))
        print("A parte real é: " + str(sub.real))
        print("A parte imaginária é: " + str(sub.imag))

    def multiplicacao(self):
        multplic = self.num1*self.num2
        print("O resultado da multiplicação é = " + str(multplic))
        print("A parte real é: " + str(multplic.real))
        print("A parte imaginária é: " + str(multplic.imag))

    def divisao(self):
        div = self.num1 / self.num2
        print("O resultado da divisão é = " + str(div))
        print("A parte real é: " + str(div.real))
        print("A parte imaginária é: " + str(div.imag))


complexo1 = NumerosComplexos((-3+6j),(5-9j))
print(complexo1.soma())
print(complexo1.subtraicao())
print(complexo1.multiplicacao())
print(complexo1.divisao())

complexo2 = NumerosComplexos(complex(-3,6), complex(9,4))
print(complexo2.soma())
print(complexo2.subtraicao())
print(complexo2.multiplicacao())
print(complexo2.divisao())

    

