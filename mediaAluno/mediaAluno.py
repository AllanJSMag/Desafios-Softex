'''Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. 
O arquivo deve ter a seguinte estrutura:
aluno: Nome do aluno;
nota_1: Primeira nota;
nota_2: Segunda nota;
faltas: Número de faltas;

O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, 
que terá a média das duas notas do aluno. A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. 
O programa deverá salvar esse novo dataframe com o nome “alunos_situacao.csv”.
Por fim, o programa deverá mostrar na tela:
- o maior número de faltas;
- a média geral das notas dos alunos;
- e a maior média.

Veja em anexo um exemplo do arquivo “notas_alunos.csv”.'''

import pandas as pd

#Buscando o arquivo "notas_alunos.csv"
df = pd.read_csv("notas_alunos.csv")

#calculando a média
media = (df["nota_1"]+ df["nota_2"])/2
df["media"] = media

#criando uma coluna "situacao"
situacao = ""
df["situacao"] = situacao

df.loc[df["media"] >= 7, "situacao"] = "APROVADO"
df.loc[df["media"] < 7, "situacao"] = "REPROVADO"
df.loc[df["faltas"] > 6, "situacao"] = "REPROVADO"

#criando variáveis para maior número de faltas, maior média e média geral 
maior_faltas = df["faltas"].max()
media_geral = df["media"].median()
maior_media = df["media"].max()

aluno_mf = df.loc[df["faltas"] == maior_faltas, ["aluno"]]
aluno_mm = df.loc[df["media"] == maior_media, ["aluno"]]

print("Maior número de faltas: ", aluno_mf.values, maior_faltas, " faltas.") 
print("Média geral das notas dos alunos: ", media_geral)
print("Maior média: ", aluno_mm.values, ", média = ", maior_media)