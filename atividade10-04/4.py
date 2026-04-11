#Leia uma palavra e mostre ela invertida.
palavra = input("Digite uma palavra: ")
palavra_invertida = palavra[::-1] #inverte a string usando slicing, onde [::-1] significa que a string deve ser lida do início ao fim, mas com um passo de -1, ou seja, de trás para frente.
print("A palavra invertida é:", palavra_invertida)

