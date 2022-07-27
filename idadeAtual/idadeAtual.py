'''Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
 A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, 
 ou completará, no ano atual (2022).
Caso o usuário não digite um número ou apareça um inválido no campo do ano, 
o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido'''

def calIdade (anoNasc, anoAtual):
    idadeAtual = anoAtual - anoNasc
    return idadeAtual

correto = 0
while correto == 0:
    try:
        nome = str(input('Informe seu nome completo: '))
        anoNasc = int(input('Informe seu ano de nascimento entre 1922 e 2021: '))
        if (1922 <= anoNasc <= 2021):
            anoAtual = 2022
            idade = calIdade(anoNasc, anoAtual)
            correto = 1
        else: raise Exception("Informe o ano no intervalo desejado!")
    
        print(nome + " sua idade é " + str(idade) + "anos!")
    except Exception as err:
        print("Ocarreu um erro.")
        print(err)
    
