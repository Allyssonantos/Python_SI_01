#Leia o valor de um compra. Se o valor for maior que 100,00, aplique um desconto.(apenas informe)

valor_compra = float(input("Digite o valor da compra: "))
if valor_compra > 100.00:
    desconto = valor_compra * 0.10  # Desconto de 10%
    valor_com_desconto = valor_compra - desconto
    print(f"O valor da compra com desconto é: R$ {valor_com_desconto:}")