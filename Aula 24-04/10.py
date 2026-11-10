# Juntar duas listas Crie duas listas e gere uma terceira contendo os elementos das duas (sem usar +).

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_combinada = []
for elemento in lista1:
    lista_combinada.append(elemento)
for elemento in lista2:
    lista_combinada.append(elemento)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista combinada:", lista_combinada)

