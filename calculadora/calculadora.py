def calculadora (num1, num2, operacao):
    if(operacao == "+"):
        res = num1+num2
    if(operacao == "-"):
        res = num1-num2
    if(operacao == "*"):
        res = num1*num2
    if(operacao == "/"):
       
        if(num2 != 0):
            if (num1%num2 != 0):
                res = int(num1/num2)
                print("resto = " + str(num1%num2))
            else:
                res = num1/num2
        else:
            res='Não existe divisão por "0".'
   
    return res
 
print("Bem-vindo! \n")
print("Que tipo de operação você quer realizar?")
 
operacao = str
cont = ""
 
while operacao != "s":
    cont = str(input('Digite "c" para continuar, ou "s" para sair\n:'))
    if(cont == "s"):
        break
    num1 = float(input('Digite o primeiro número:'))
    num2 = float(input('Digite o segundo número:'))
    operacao = str(input('Digite \n "+" para soma;\n "-" subtração;\n "*" multiplicação;\n "/" divisão;\n:'))
    print("\n")
    resultado = calculadora(num1, num2, operacao)
    print("O resultado esperado é = " + str(resultado))
    print("\n")
 
print("Até a próxima!")
