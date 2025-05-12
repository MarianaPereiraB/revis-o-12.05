soma = 0
for w in range(1, 6):
    num = int(input(f"digite a {w}° nota: "))
    soma += num
    media = soma / 5
    print(f"sua média é {media}")
    if media >= 7:
        print("e voce foi aprovado")
    elif media < 4:
        print("e voce foi reprovado")
    elif media  >4 and media <7:
        print("e você está na recuperação")
