"""Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento. 
Depois, desenvolva três ou mais objetos para testar o código."""

class Aluno:
    def __init__(self, nome, turma, nota1:float, nota2:float):
        self.nome = nome
        self.turma = turma
        self.nota1 = nota1
        self.nota2 = nota2

    def get_media(self):
        return (self.nota1 + self.nota2)/2

    def aprovado(self):
        return self.get_media() >= 7

    def __str__(self):
        txt = 'Nome: ' + self.nome 
        txt += '\nTurma: ' + self.turma
        txt += '\nNotas: %2.1f, %2.1f' %(self.nota1, self.nota2)
        txt += '\nMédia: %2.1f' % self.get_media()
        txt += ' ** %s **\n' % ('aprovado' if self.aprovado() else 'reprovado')
        return txt


a1 = Aluno("José da Silva", "2º A", 10, 6.5)
a2 = Aluno("Fracisco Jr.", "1º B", 2.75, 7.25)
a3 = Aluno("Maria Eduarda", "9º A", 7.6, 8.0)

print (a1.__str__())
print (a2.__str__())
print (a3.__str__())
