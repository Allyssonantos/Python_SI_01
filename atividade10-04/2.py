#Leia um número e verifique se é par ou ímpar.
num = int(input("Digite um número interiro: "))

if num %  2 == 0: #verifica se o número é par, se o resto da divisão por 2 for igual a zero, o número é par.
    print("o número é par.")
else: #se o número não for par, ele é ímpar.
    print("o número é ímpar.")
