#Receba a idade de uma pessoa e classifique: Criança (0–12),Adolescente (13–17), Adulto (18–59), Idoso (60+)
print('-'*20)
idade = int(input("Digite a idade da pessoa: "))
print('-'*20)

if idade >= 0 and idade <=12:
    print("Criança")
elif idade >= 13 and idade <=17:
    print("Adolescente")
elif idade >= 18 and idade <=59:
    print("Adulto")
elif idade >=60:
    print("Idoso")


