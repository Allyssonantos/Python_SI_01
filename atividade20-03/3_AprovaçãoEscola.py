#Leia a nota de um aluno (0 a 10). Se for maior ou igual a 7, está aprovado, caso contrário, re

nota = float(input("Digite a nota do aluno (0 a 10): "))

if nota >= 6:
    print("O aluno está aprovado.")
else:
    print("O aluno está reprovado.")