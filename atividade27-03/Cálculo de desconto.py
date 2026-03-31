#Peça o valor da compra:
#Se maior que 100:
#Cliente VIP → 20% desconto
#Cliente comum → 10% desconto
#Senão → sem desconto


print('='*40)
valor_compra = float(input("Digite o valor da compra: "))
print('='*40)
if valor_compra > 100:
    tipo_cliente = input("Digite o tipo de cliente (VIP ou comum): ")
    print('='*40)
    if tipo_cliente.lower() == "vip":
        desconto = valor_compra * 0.20
        valor_final = valor_compra - desconto
        print("Valor final com desconto VIP:", valor_final)
    elif tipo_cliente.lower() == "comum":
        desconto = valor_compra * 0.10
        valor_final = valor_compra - desconto
        print("Valor final com desconto comum:", valor_final)
    else:
        print("Tipo de cliente inválido.")
else:
    print("Valor final sem desconto:", valor_compra)

    