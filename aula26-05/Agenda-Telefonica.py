#Faça um program em python para armazenar nomes de uma agenda telefonica contendo nome, endereço, telefone e data de nascimento.

def cab():
    print("-" * 30)
    print("AGENDA TELEFONICA")
    print("-" * 30)

print("Bem Vindo a sua Agenda Telefonica")

nome = ""

while True:
    cab()
    print()
    nome = input("Nome: ").strip()
    if nome.upper() == "FIM":
        break

    ende = input("Endereço: ")
    tel = input("Telefone: ")
    data = input("Data de Nascimento: ")

    with open("Agenda-Telefonica/agenda.txt", "a") as dados:
        dados.write(f"Nome: {nome}\n")
        dados.write(f"Endereço: {ende}\n")
        dados.write(f"Telefone: {tel}\n")
        dados.write(f"Data de Nascimento: {data}\n")
        dados.write("-" * 30 + "\n")