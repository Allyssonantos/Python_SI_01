import os
import cadastro
import consulta
import exclusao


def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n== SISTEMA DE CLIENTES ==")
        print("1 - Cadastrar Cliente")
        print("2 - Consultar Cliente")
        print("3 - Excluir Cliente")
        print("4 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastro.cadastrar()
        elif opcao == "2":
            consulta.consultar()
        elif opcao == "3":
            exclusao.excluir()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    menu()