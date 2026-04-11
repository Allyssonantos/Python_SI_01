#Leia um número e imprima sua tabuada usando for.
num = int(input("Digite um número inteiro: "))
print("Tabuada de", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
