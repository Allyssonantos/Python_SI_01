#faça um programa em python para armazenar dados de clientes em um arquivo de texto os clientes devem ser compostos por Cód, Nome, Teledone, E-mail, Cidade, Estado, CPF/CNPJ, Tipo (PF/PJ), DataCadastro.

def cab():
    print("-" * 30)
    print("DADOS DE CLIENTES")
    print("-" * 30)

print("Bem Vindo ao Cadastro de Clientes")
cod = 0
while True:
    cab()
    print()
    cod += 1
    nome = input("Nome: ").strip()
    if nome.upper() == "FIM":
        break

    tel = input("Telefone: ")
    email = input("E-mail: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cpf_cnpj = input("CPF/CNPJ: ")
    tipo = input("Tipo (PF/PJ): ")
    data_cadastro = input("Data de Cadastro: ")

    with open("aula26-05/clientes.txt", "a") as dados:
        dados.write(f"Cód: {cod}\n")
        dados.write(f"Nome: {nome}\n")
        dados.write(f"Telefone: {tel}\n")
        dados.write(f"E-mail: {email}\n")
        dados.write(f"Cidade: {cidade}\n")
        dados.write(f"Estado: {estado}\n")
        dados.write(f"CPF/CNPJ: {cpf_cnpj}\n")
        dados.write(f"Tipo: {tipo}\n")
        dados.write(f"Data de Cadastro: {data_cadastro}\n")
        dados.write("-" * 30 + "\n")

