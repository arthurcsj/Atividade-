nome=(input("digite seu nome: "))
senha= (input("digite sua senha: "))

while nome == senha:
    print("senha igual nome nao e permitida")
    print("tente novamente")
    nome=(input("digite seu nome: "))
    senha= (input("digite sua senha: "))
else:
    print("cadastro completo")
    print("obrigado por fazer seu cadastro")
    