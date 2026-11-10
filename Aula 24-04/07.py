 #Procurar um valor Peça um número ao usuário e verifique se ele está presente na lista.
numeros = [1, 2, 3, 4, 5]
numero_usuario = int(input("Digite um número para verificar se está na lista: "))
encontrado = False
for numero in numeros:
    if numero == numero_usuario:
        encontrado = True
        break
if encontrado:
    print("O número está presente na lista.")
else:
    print("O número não está presente na lista.")

    