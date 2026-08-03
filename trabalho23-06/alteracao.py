import os
import ast


def alterar():
    os.system("cls" if os.name == "nt" else "clear")
    print("== ALTERAR CLIENTE ==\n")

    # Busca o cliente pelo CPF
    cpf = input("Digite o CPF do cliente: ").strip()

    # Verifica se o arquivo de clientes existe
    if not os.path.exists("clientes.txt"):
        print("\nNenhum cliente cadastrado ainda.")
        input("\nPressione Enter para continuar...")
        return

    clientes = []

    # Lê todos os clientes do arquivo
    with open("clientes.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            try:
                clientes.append(ast.literal_eval(linha))
            except (ValueError, SyntaxError):
                continue

    # Procura o cliente com o CPF informado
    cliente_encontrado = None
    for c in clientes:
        if c["cpf"] == cpf:
            cliente_encontrado = c
            break

    if cliente_encontrado is None:
        print("\nCliente não encontrado.")
        input("\nPressione Enter para continuar...")
        return

    print(f"\nCliente encontrado: {cliente_encontrado['nome']}")
    print("\nDeixe em branco para manter o valor atual.\n")

    # Coleta os novos dados, mantendo o valor atual se deixado em branco
    nome     = input(f"Nome [{cliente_encontrado['nome']}]: ").strip()
    telefone = input(f"Telefone [{cliente_encontrado['telefone']}]: ").strip()
    email    = input(f"E-mail [{cliente_encontrado['email']}]: ").strip()
    endereco = input(f"Endereço [{cliente_encontrado['endereco']}]: ").strip()
    cidade   = input(f"Cidade [{cliente_encontrado['cidade']}]: ").strip()
    estado   = input(f"Estado [{cliente_encontrado['estado']}]: ").strip()

    # Atualiza apenas os campos que foram preenchidos
    if nome:     cliente_encontrado["nome"]     = nome
    if telefone: cliente_encontrado["telefone"] = telefone
    if email:    cliente_encontrado["email"]    = email
    if endereco: cliente_encontrado["endereco"] = endereco
    if cidade:   cliente_encontrado["cidade"]   = cidade
    if estado:   cliente_encontrado["estado"]   = estado

    # Salva todos os clientes de volta no arquivo com os dados atualizados
    with open("clientes.txt", "w") as arquivo:
        for c in clientes:
            arquivo.write(str(c) + "\n")

    print("\nCliente alterado com sucesso!")
    input("\nPressione Enter para continuar...")