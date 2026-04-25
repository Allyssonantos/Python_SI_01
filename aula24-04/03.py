#Contar números pares Crie uma lista com 15 números e conte quantos são pares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
contador_pares = 0
for numero in numeros:
    if numero % 2 == 0:
        contador_pares += 1
print("A quantidade de números pares na lista é:", contador_pares)
