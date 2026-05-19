#faça um jogo da forca, onde o jogador tem 6 chances para acertar a palavra, caso erre as 6 chances, ele perde o jogo, caso acerte a palavra, ele ganha o jogo

import random
frutas = ["banana", "abacaxi", "laranja", "uva", "melancia", "morango", "pera", "caju", "goiaba", "manga"]
def boneco(erro):
    if (erro == 0):
        print(" ______    ")
        print("|/   (   ) ")
        print("|          ")
        print("|          ")
        print("|          ")
    elif (erro == 1):         
        print(" ______")
        print("|/   ( O ) ")
        print("|          ")
        print("|          ")
        print("|          ")
    elif (erro == 2):
        print(" ______")
        print("|/   ( O ) ")   
        print("|      |   ")
        print("|      |   ")
        print("|          ")
    elif (erro == 3):
        print(" ______")
        print("|/   ( O ) ")  
        print("|     \|   ")
        print("|      |   ")
        print("|          ")
    elif (erro == 4):
        print(" ______")
        print("|/   ( O ) ")   
        print("|     \|/  ")
        print("|      |   ")
        print("|          ")
    elif (erro == 5):
        print(" ______")
        print("|/   ( O ) ")   
        print("|     \|/  ")
        print("|      |   ")
        print("|     /    ")
    elif (erro == 6):
        print(" ______")
        print("|/   ( O ) ")   
        print("|     \|/  ")
        print("|      |   ")
        print("|     / \  ")
    elif (erro == 7):

        print(" ______")
        print("|/   ( O ) ")   
        print("|     \|/  ")
        print("|      |   ")
        print("|     / \  ")
        print("|          ")
        print("|          ")
def jogo():


    palavra = random.choice(frutas)
    letras_acertadas = []
    letras_erradas = []
    erro = 0
    while True:
        boneco(erro)
        print("Palavra: ", end="")
        for letra in palavra:
            if letra in letras_acertadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print("\nLetras erradas: ", end="")
        for letra in letras_erradas:
            print(letra, end=" ")
        print("\n")
        letra = input("Digite uma letra: ")
        if letra in palavra:
            letras_acertadas.append(letra)
            if len(letras_acertadas) == len(set(palavra)):
                print("Parabéns, você ganhou!")
                break
        else:
            letras_erradas.append(letra)
            erro += 1
            if erro == 6:
                boneco(erro)
                print("Você perdeu! A palavra era: ", palavra)
                break
            