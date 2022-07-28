'''Desenvolva um código que simule uma eleição com três candidatos.
- candidato_X => 889
- candidato_Y => 847
- candidato_Z => 515
- branco => 0

O código deve perguntar se deseja finalizar a votação depois do voto.
Caso o número do voto não corresponda a nenhum candidato ou seja branco, ele deve ser tratado como nulo. 
Se for inserido um texto ao invés de número, o código deve retornar uma mensagem para votar novamente.

Quando a votação for finalizada, o código deverá mostrar o vencedor, 
aquele com o maior número de votos e, também, a quantidade de votos de cada candidato, os brancos e nulos '''


numEleitores = 10
x = 0
y = 0
z = 0
brancos = 0
nulos = 0

for i in range(numEleitores):
    cont = 0
    while cont == 0:
        try:
            voto = int(input('Digite o número do candidato: '))
            final = input('Finalizar votação? \nDigite: "s" para sim ou "n" para não:')
            if(final == "s"):
                if(voto == 889):
                    x = x + 1
                elif(voto == 847):
                    y = y + 1
                elif(voto == 515):
                    z = z + 1
                elif(voto == 0):
                    brancos = brancos + 1
                else:
                    nulos = nulos + 1
                cont = 1
        except:
            print("Por favor, incerir apenas números!\nVotar novamete!")

if(x > y) and (x > z):
    print("O Candidato_X ganhou com " + str(x) + " votos!")
    if(y > z):
        print("Candidato_Y: " + str(y) + " votos!")
        print("Candidato_Z: " + str(z) + " votos!")
    else:
        print("Candidato_Z: " + str(z) + " votos!")
        print("Candidato_Y: " + str(y) + " votos!")
elif(y > x) and (y > z):
    print("O Candidato_Y ganhou com " + str(y) + " votos!")
    if(x > z):
        print("Candidato_X: " + str(x) + " votos!")
        print("Candidato_Z: " + str(z) + " votos!")
    else:
        print("Candidato_Z: " + str(z) + " votos!")
        print("Candidato_X: " + str(x) + " votos!")
elif(z > x) and (z > y):
    print("O Candidato_Z ganhou com " + str(z) + " votos!")
    if(x > y):
        print("Candidato_X: " + str(x) + " votos!")
        print("Candidato_Y: " + str(y) + " votos!")
    else:
        print("Candidato_Y: " + str(y) + " votos!")
        print("Candidato_X: " + str(x) + " votos!")
else:
    print("Houve empate!\n")
    print("Candidato_X: " + str(x) + " votos!")
    print("Candidato_Y: " + str(y) + " votos!")
    print("Candidato_Z: " + str(z) + " votos!")

print("Votos brancos: " + str(brancos) + " votos!")
print("Votos nulos: " + str(nulos) + " votos!")
        