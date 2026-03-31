
saldo =float(input("Digite o saldo da conta: "))
print('='*40)
valor_saque = float(input("Digite o valor do saque: "))
print('='*40)
if valor_saque <= saldo:
    saldo -= valor_saque
    print("Saque realizado com sucesso. Saldo restante:", saldo)
else:
    print("Saldo insuficiente para realizar o saque.")

