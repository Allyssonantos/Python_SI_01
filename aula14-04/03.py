print("-" * 30)
print("Programa de listas")
print("-" * 30)

lista = []

while True:
    nome = input("Nome (ou FIM para encerrar): ")
    if nome.upper() == "FIM":
        break

    endereco = input("Endereço: ") 
    telefone = input("Telefone: ")
    salario = float(input("Salário: "))
    lista.append([nome, endereco, telefone, salario])






    
