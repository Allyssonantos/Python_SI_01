import os
import ast


def consultar():
    os.system("cls" if os.name == "nt" else "clear")
    print("== CONSULTA DE CLIENTES ==")
    print("1 - Buscar por Nome")
    print("2 - Buscar por CPF")
    print("3 - Buscar por Código")
    print("0 - Voltar")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "0":
        return

    if opcao not in ("1", "2", "3"):
        print("Opção inválida.")
        input("Pressione Enter para continuar...")
        return

    termo = input("Digite o termo de busca: ").strip().lower()

    if not os.path.exists("clientes.txt"):
        print("\nNenhum cliente cadastrado ainda.")
        input("Pressione Enter para continuar...")
        return

    resultados = []

    with open("clientes.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            try:
                cliente = ast.literal_eval(linha)
            except (ValueError, SyntaxError):
                continue

            if opcao == "1" and termo in cliente.get("nome", "").lower():
                resultados.append(cliente)
            elif opcao == "2" and termo in cliente.get("cpf", "").lower():
                resultados.append(cliente)
            elif opcao == "3" and termo in cliente.get("codigo", "").lower():
                resultados.append(cliente)

    if not resultados:
        print("\nNenhum cliente encontrado.")
    else:
        print(f"\n{len(resultados)} cliente(s) encontrado(s):\n")
        for c in resultados:
            print("-" * 40)
            print(f"  Código   : {c.get('codigo', '-')}")
            print(f"  Nome     : {c.get('nome', '-')}")
            print(f"  CPF      : {c.get('cpf', '-')}")
            print(f"  Telefone : {c.get('telefone', '-')}")
            print(f"  E-mail   : {c.get('email', '-')}")
            print(f"  Endereço : {c.get('endereco', '-')}")
            print(f"  Cidade   : {c.get('cidade', '-')} - {c.get('estado', '-')}")
        print("-" * 40)

    input("\nPressione Enter para continuar...")