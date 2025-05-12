senha = 1234
digite = 0
while digite != senha:
    digite = int(input("digite a senha: "))
    if digite == senha:
        print("Acesso liberado")
    else:
        print("tente novamente")
