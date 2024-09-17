a = int(input("Escreva seu número inteiro: "))
if (a % 3 ==0 & a % 5==0):
    print ("É divisivel por ambos!")
elif (a % 3==0):
    print ("É divisivel apenas pelo 3!")
elif (a % 5==0):
    print("É divisivel apenas pelo 5!")
else:
    print ("Não é divisivel por nenhum!")
