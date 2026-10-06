#Crei um program que onde o usuário possa digitar sete valores numéricos e cadastre-os em uma "lista unica" e mantenha separados os numeros pares dos impares em ordem crescente.

numeros = [] # lista para armazenar todos os números
pares = [] # lista para armazenar os números pares
impares = [] # lista para armazenar os números ímpares

for i in range(7): # loop para solicitar 7 números
    num = int(input(f"Digite o {i+1}º número: ")) # solicita o número ao usuário
    numeros.append(num) # adiciona o número à lista de todos os números
    if num % 2 == 0: # verifica se o número é par
        pares.append(num) # adiciona à lista de pares
    else:
        impares.append(num) # adiciona à lista de ímpares

pares.sort() # ordena a lista de números pares em ordem crescente
impares.sort() # ordena a lista de números ímpares em ordem crescente

print(f"\nTodos os números digitados: {numeros}") # exibe todos os números digitados
print(f"Números pares em ordem crescente: {pares}") # exibe os números pares
print(f"Números ímpares em ordem crescente: {impares}") # exibe os números ímpares

