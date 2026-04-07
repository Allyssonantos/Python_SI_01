#Calculadora
#1 - Adição
#2 - Subtração
#3 - Multiplicação
#4 - Divisão

print("-"*40)
print("OPERAÇÕES")
print("-"*40)

print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Sair")

operacao = int(input("Escolha uma operação: "))

while operacao != 5:
    if operacao == 1:
        num1 = float(input("digite o primeiro numero: "))
        num2 = float(input("digite o segundo numero: "))
        resultado = num1 + num2
        print("O resultado da adição é: ", resultado)
    elif operacao == 2:
        num1 = float(input("digite o primeiro numero:"))
        num2 = float(input("digite o segundo numero:"))
        resultado = num1 - num2
        print("O resultado da subtração é: ", resultado)
    elif operacao == 3:
        num1 = float(input("digite o primeiro numero:"))
        num2 = float(input("digite o segundo numero:"))
        resultado = num1 * num2
        print("O resultado da multiplicação é: ", resultado)
    elif operacao == 4:
        num1 = float(input("digite o primeiro numero:"))
        num2 = float(input("digite o segundo numero:"))
        if num2 != 0:
            resultado = num1 / num2
            print("O resultado da divisão é: ", resultado)
        else:
            print("Não é possível dividir por zero.")
    
print("Encerrando a calculadora. Obrigado por usar!")

