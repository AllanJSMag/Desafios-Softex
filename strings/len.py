"""Estruture três códigos, os quais devem conter uma função de manipulação de string que obtenha resultado."""

#Usando o método 'len'

animal = input('Informe o nome de um animal que tem 6 letras e inicia com a letra "J": ')

a = animal[0]
letras = len(animal)

if( a.upper() == 'J' and letras == 6):
    print('Parabens! Nome valido!')
else:
    print('Nome inválido!')
