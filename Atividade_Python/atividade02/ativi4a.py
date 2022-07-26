senha1=(input("digite sua senha: "))
senha2= (input("digite novamente sua senha: "))

while senha1 != senha2:
    print("sua senha deve ser igual")
    print("tente novamente")
    senha2=input()
else:
    print("senha correta")
