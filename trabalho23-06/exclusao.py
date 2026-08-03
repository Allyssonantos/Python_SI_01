import os
import ast


def excluir():
    os.system("cls" if os.name == "nt" else "clear")
    print("== EXCLUIR CLIENTE ==\n")
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

    # Filtra os clientes que correspondem ao termo buscado
    resultados = []
    for c in clientes:
        if opcao == "1" and termo in c["nome"]:
            resultados.append(c)
        elif opcao == "2" and termo in c["cpf"]:
            resultados.append(c)
        elif opcao == "3" and termo in c["codigo"]:
            resultados.append(c)

    if not resultados:
        print("\nNenhum cliente encontrado.")
        input("\nPressione Enter para continuar...")
        return

    # Exibe a lista de clientes encontrados para o usuário escolher
    print(f"\n{len(resultados)} cliente(s) encontrado(s):\n")
    for i, c in enumerate(resultados, 1):
        print(f"[{i}] {c['nome']} | CPF: {c['cpf']} | Código: {c['codigo']}")
    print("\n[0] Cancelar")

    escolha = input("\nDigite o número do cliente a excluir: ").strip()

    if escolha == "0":
        print("Operação cancelada.")
        input("\nPressione Enter para continuar...")
        return

    if not escolha.isdigit() or not (1 <= int(escolha) <= len(resultados)):
        print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        return

    # Pega o cliente selecionado da lista
    cliente_excluir = resultados[int(escolha) - 1]

    # Exibe os dados do cliente para confirmação
    print(f"\nTem certeza que deseja excluir o cliente abaixo?")
    print(f"  Nome   : {cliente_excluir['nome']}")
    print(f"  CPF    : {cliente_excluir['cpf']}")
    print(f"  Código : {cliente_excluir['codigo']}")

    confirmacao = input("\nDigite S para confirmar: ").strip().upper()

    if confirmacao != "S":
        print("Exclusão cancelada.")
        input("\nPressione Enter para continuar...")
        return

    # Remove o cliente da lista e salva o arquivo atualizado
    atualizados = [c for c in clientes if c["codigo"] != cliente_excluir["codigo"]]
    with open("clientes.txt", "w") as arquivo:
        for c in atualizados:
            arquivo.write(str(c) + "\n")

    print(f"\nCliente '{cliente_excluir['nome']}' excluído com sucesso!")
    input("\nPressione Enter para continuar...")