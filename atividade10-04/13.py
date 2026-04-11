#Conte quantos números pares existem entre 1 e 50.

contador_pares = 0
for num in range(1, 51):
    if num % 2 == 0:
        contador_pares += 1
print("Existem", contador_pares, "números pares entre 1 e 50.")





