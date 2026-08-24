cadastros = []

while True:
    print("\n===== SISTEMA DE CADASTRO =====")
    print("1 - Cadastrar")
    print("2 - Consultar cadastros")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ").strip()
        while not nome:
            print("Nome não pode ficar vazio.")
            nome = input("Nome: ").strip()

        idade = input("Idade: ").strip()
        while not idade.isdigit():
            print("Idade deve ser um número.")
            idade = input("Idade: ").strip()

        sexo = input("Sexo (M/F): ").strip().upper()
        while sexo not in ["M", "F"]:
            print("Sexo inválido. Digite M ou F.")
            sexo = input("Sexo (M/F): ").strip().upper()

        termos = input("Aceita os termos? (s/n): ").strip().lower()
        while termos not in ["s", "n"]:
            print("Resposta inválida. Digite s ou n.")
            termos = input("Aceita os termos? (s/n): ").strip().lower()

        if termos == "n":
            print("Cadastro cancelado. Você precisa aceitar os termos.")
            continue

        print("Disciplinas disponíveis:")
        disciplinas = ["Banco de Dados", "Redes", "Programação Web", "Sistemas Operacionais"]
        for i, item in enumerate(disciplinas, 1):
            print(f"{i} - {item}")

        escolhas = input("Escolha as disciplinas pelo número separados por vírgula (ex: 1,3): ").strip()
        lista_disciplinas = []

        if escolhas:
            for item in escolhas.split(","):
                num = item.strip()
                if num.isdigit() and 1 <= int(num) <= len(disciplinas):
                    lista_disciplinas.append(disciplinas[int(num) - 1])

        cadastros.append({
            "nome": nome,
            "idade": idade,
            "sexo": sexo,
            "disciplinas": lista_disciplinas if lista_disciplinas else ["Nenhuma disciplina selecionada"]
        })

        print("\nCadastro realizado com sucesso!")

    elif opcao == "2":
        if not cadastros:
            print("Nenhum cadastro realizado.")
        else:
            print("\n=== CADASTROS ===")
            for i, c in enumerate(cadastros, 1):
                print(f"{i}. Nome: {c['nome']} | Idade: {c['idade']} | Sexo: {c['sexo']} | Disciplinas: {', '.join(c['disciplinas'])}")

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")