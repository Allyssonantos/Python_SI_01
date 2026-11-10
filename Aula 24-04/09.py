# Ordenar lista (Bubble Sort) Implemente uma ordenação crescente usando for ou while.

numeros = [64, 34, 25, 12, 22, 11, 90]
n = len(numeros)
for i in range(n):
    for j in range(0, n - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
print("Lista ordenada:", numeros)

