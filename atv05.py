#crie um programa e peça ao usuário para digitar 5 números e usando for calcule a média aritmética
soma = 0
for w in range(1,6):
    num = int(input(f"digite a {w}° nota: "))
    soma += num
    media = soma/5
print(f"a sua média é {media}")
