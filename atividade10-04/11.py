#Leia um número e calcule o fatorial usando while.
num = int(input("Digite um número inteiro: "))
fatorial = 1
contador = 1
while contador <= num:
    fatorial *= contador 
    contador += 1
print("O fatorial de", num, "é:", fatorial)

