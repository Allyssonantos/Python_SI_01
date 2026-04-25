#Contar ocorrências Dada uma lista, conte quantas vezes um determinado número aparece.
numeros = [1, 2, 3, 4, 5, 2, 3, 2]
numero_usuario = int(input("Digite um número para contar suas ocorrências na lista: "))
contador_ocorrencias = 0
for numero in numeros:
    if numero == numero_usuario:
        contador_ocorrencias += 1
print(f"O número {numero_usuario} aparece {contador_ocorrencias} vezes na lista.")

