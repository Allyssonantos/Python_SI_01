def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return numero


def leiaFloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem).replace(',', '.'))
        except (ValueError, TypeError): #serve para capturar dois tipos de erro, caso o usuário digite um valor inválido
            print('\033[31mERRO! Digite um número real válido.\033[m') #serve para imprimir a mensagem de erro em vermelho
        else:
            return numero

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')

print(f'Você digitou o número inteiro {n1}.')
print(f'Você digitou o número real {n2}.')