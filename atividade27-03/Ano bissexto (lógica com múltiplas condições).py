#Ano bissexto (lógica com múltiplas condições)
#Peça um ano e determine se é bissexto:
#Divisível por 4
#Mas não por 100, exceto se for divisível por 400


print('='*40)
ano = int(input("Digite um ano: "))
print('='*40)
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")

