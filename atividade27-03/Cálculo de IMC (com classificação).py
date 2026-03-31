#Peça peso e altura, calcule o IMC:
#IMC < 18.5 → Abaixo do peso
#18.5–24.9 → Normal
#25–29.9 → Sobrepeso
#≥ 30 → Obesidade

print('='*40)
peso = float(input("Digite o peso em kg: "))
print('='*40)
altura = float(input("Digite a altura em metros: "))
print('='*40)
imc = peso / (altura ** 2)
print("O IMC é:", imc)
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")

    