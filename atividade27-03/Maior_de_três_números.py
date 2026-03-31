#Leia três números e determine qual é o maior.
#Verificção de triângulo (com aninhamento)
#Peça três valores e verifique:
#Se podem formar um triângulo
#Se sim, classifique:
#Equilátero (todos iguais)
#Isósceles (dois iguais)
#Escaleno (todos diferentes)

print('='*40)
num1 = float(input("Digite o primeiro número: "))
print('='*40)
num2 = float(input("Digite o segundo número: "))
print('='*40)
num3 = float(input("Digite o terceiro número: "))
print('='*40)

if num1 >= num2 and num1 >= num3:
    print("O maior número é:", num1)
elif num2 >= num1 and num2 >= num3:
    print("O maior número é:", num2)
else:
    print("O maior número é:", num3)




