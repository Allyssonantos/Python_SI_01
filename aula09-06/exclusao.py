import os
import ast


def excluir():
    os.system("cls" if os.name == "nt" else "clear")
    print("== EXCLUIR CLIENTE ==")
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

    clientes = []

    with open("clientes.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            try:
                cliente = ast.literal_eval(linha)
                clientes.append(cliente)
            except (ValueError, SyntaxError):
                continue

    resultados = []

    for c in clientes:
        if opcao == "1" and termo in c.get("nome", "").lower():
            resultados.append(c)
        elif opcao == "2" and termo in c.get("cpf", "").lower():
            resultados.append(c)
        elif opcao == "3" and termo in c.get("codigo", "").lower():
            resultados.append(c)

    if not resultados:
        print("\nNenhum cliente encontrado.")
        input("Pressione Enter para continuar...")
        return

    print(f"\n{len(resultados)} cliente(s) encontrado(s):\n")
    for i, c in enumerate(resultados, 1):
        print(f"[{i}] {c.get('nome', '-')} | CPF: {c.get('cpf', '-')} | Código: {c.get('codigo', '-')}")

    print("\n[0] Cancelar")
    escolha = input("\nDigite o número do cliente a excluir: ").strip()

    if escolha == "0":
        print("Operação cancelada.")
        input("Pressione Enter para continuar...")
        return

    if not escolha.isdigit() or not (1 <= int(escolha) <= len(resultados)):
        print("Opção inválida.")
        input("Pressione Enter para continuar...")
        return

    cliente_excluir = resultados[int(escolha) - 1]

    print(f"\nTem certeza que deseja excluir o cliente abaixo?")
    print(f"  Nome   : {cliente_excluir.get('nome', '-')}")
    print(f"  CPF    : {cliente_excluir.get('cpf', '-')}")
    print(f"  Código : {cliente_excluir.get('codigo', '-')}")

    confirmacao = input("\nDigite S para confirmar: ").strip().upper()

    if confirmacao != "S":
        print("Exclusão cancelada.")
        input("Pressione Enter para continuar...")
        return

    clientes_atualizados = [c for c in clientes if c.get("codigo") != cliente_excluir.get("codigo")]

    with open("clientes.txt", "w") as arquivo:
        for c in clientes_atualizados:
            arquivo.write(str(c) + "\n")

    print(f"\nCliente '{cliente_excluir.get('nome')}' excluído com sucesso!")
    input("Pressione Enter para continuar...")