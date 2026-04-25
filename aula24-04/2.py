#Maior valor da lista Dada uma lista de números, encontre o maior valor sem usar max().

numeros = [3, 7, 2, 9, 5]
maior = numeros[0]  # Inicializa o maior com o primeiro elemento da lista
for numero in numeros:
    if numero > maior:
        maior = numero
print("O maior valor da lista é:", maior)

