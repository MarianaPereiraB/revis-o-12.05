'''escreva um programa que receba 5 nomes e print só os que tem a letra "A" '''
nomes= []
for x in range (5):
    nome = input("digite 5 nomes: ")
    nomes.append(nome)
for nome in nomes:
    if nome [0] =="a" or nome [0] == "A":
        print(nome)
nomes = []
for x in range(5):
    nome = input("digite um nome: ")
    nomes.append(nome)
for nome in nomes:
    if nome [0] == "a" or nome [0] == "A":
        print(nome)