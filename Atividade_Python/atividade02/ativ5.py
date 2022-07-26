nota= int((input("digite uma nota:")))
while nota < 0 or nota > 10:
    print("digite uma nota de 0 a 10")
    nota  = int(input())
else:
    print("valido")
