#Peça duas notas e calcule a média: Média ≥ 7 → Aprovado, Média entre 5 e 6.9 → Recuperação, Média < 5 → Reprovado

print('='*40)
nota1 = float(input("Digite a primeira nota: "))
print('='*40)
nota2 = float(input("Digite a segunda nota: "))
print('='*40)

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
else:
    print("Reprovado")
