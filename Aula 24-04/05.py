#Média dos valores Calcule a média dos valores de uma lista de números.

numeros = [10, 20, 30, 40, 50]
soma = 0
for numero in numeros:
    soma += numero
media = soma / len(numeros)
print("A média dos valores é:", media)

