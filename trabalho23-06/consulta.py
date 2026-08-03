import os
import ast


def consultar():
    os.system("cls" if os.name == "nt" else "clear")
    print("== CONSULTA DE CLIENTES ==\n")
    print("1 - Buscar por Nome")
    print("2 - Buscar por CPF")
    print("3 - Buscar por Código")
    print("0 - Voltar")

    opcao = input("\nEscolha uma opção: ").strip()

    # Retorna ao menu principal
    if opcao == "0":
        return

    if opcao not in ("1", "2", "3"):
        print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        return

    termo = input("Digite o termo de busca: ").strip()

    # Verifica se o arquivo de clientes existe
    if not os.path.exists("clientes.txt"):
        print("\nNenhum cliente cadastrado ainda.")
        input("\nPressione Enter para continuar...")
        return

    resultados = []

    # Lê o arquivo e converte cada linha de volta para dicionário
    with open("clientes.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            try:
                cliente = ast.literal_eval(linha)
            except (ValueError, SyntaxError):
                continue

            # Compara o termo digitado com o campo escolhido
            if opcao == "1" and termo in cliente["nome"]:
                resultados.append(cliente)
            elif opcao == "2" and termo in cliente["cpf"]:
                resultados.append(cliente)
            elif opcao == "3" and termo in cliente["codigo"]:
                resultados.append(cliente)

    # Exibe os resultados encontrados
    if not resultados:
        print("\nNenhum cliente encontrado.")
    else:
        print(f"\n{len(resultados)} cliente(s) encontrado(s):\n")
        for c in resultados:
            print("-" * 40)
            print(f"  Código   : {c['codigo']}")
            print(f"  Nome     : {c['nome']}")
            print(f"  CPF      : {c['cpf']}")
            print(f"  Telefone : {c['telefone']}")
            print(f"  E-mail   : {c['email']}")
            print(f"  Endereço : {c['endereco']}")
            print(f"  Cidade   : {c['cidade']} - {c['estado']}")
        print("-" * 40)

    input("\nPressione Enter para continuar...")