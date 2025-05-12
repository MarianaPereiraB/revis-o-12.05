adivinha = 22
chute = 0
while adivinha != chute:
    chute = int(input("adivinhe um número entre 1 e 100: "))
    if chute < adivinha :
        print("muito baixo")
    elif chute > adivinha:
        print("muito alto")
    else:
        print("parabéns arrasou")