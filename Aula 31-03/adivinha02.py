print("-------------------------------")
print("Adivinhe o Numero de 0 a 100")
print("-------------------------------")

numero_secreto = 53

while True:
    chute = int(input("Digite o numero: "))

    if chute == numero_secreto:
        print("Parabens, voce acertou!")
    elif chute < numero_secreto:
        print("O numero secreto e maior")
    else:
        print("O numero secreto e menor")






        
    


