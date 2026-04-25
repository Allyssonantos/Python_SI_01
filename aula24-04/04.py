# Inverter lista manualmente Dada uma lista, crie outra lista com os elementos na ordem inversa (sem usar .reverse()).

numeros = [1, 2, 3, 4, 5]
lista_invertida = []
for i in range(len(numeros) - 1, -1, -1):
    lista_invertida.append(numeros[i])
print("Lista original:", numeros)
print("Lista invertida:", lista_invertida)

