#Remover valores negativos D ada uma lista com números positivos e negativos, crie uma nova lista contendo apenas os valores positivos.

numeros = [3, -1, 5, -2, 7, -4]
numeros_positivos = []
for numero in numeros:
    if numero > 0:
        numeros_positivos.append(numero)
print("Lista original:", numeros)
print("Lista com apenas valores positivos:", numeros_positivos)
