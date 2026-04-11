print("-------------------------------")
print("Adivinhe o Numero de 0 a 100")
print("-------------------------------")
print()
print("Qual é o nivel de dificuldade?")
print("1 - Facil")
print("2 - Medio")
print("3 - Dificil")
print()

total_chutes = 0
numero_secreto = 53

nivel = int(input("Escolha o nivel de dificuldade: "))

if nivel == 1:
    total_chutes = 20
elif nivel == 2:
    total_chutes = 11
elif nivel == 3:   
    total_chutes = 7

for rodada in range(1, total_chutes + 1):
    print("Rodada {} de {}".format(rodada, total_chutes))
    chute = int(input("Digite o numero: "))

    if chute == numero_secreto:
        print("Parabens, voce acertou!")
        break
    elif chute < numero_secreto:
        print("O numero secreto e maior")
    else:
        print("O numero secreto e menor")

