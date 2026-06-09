import os
import cadastro
import consulta

def menu():
    while True:
        os.system("clear")
        print("\n1 - Cadastrar Cliente")
        print("2 - Consultar Cliente")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ").split()

        if opcao[0] == "1":
            cadastro.cadastrar()
        elif opcao[0] == "2":
            consulta.consultar()
        elif opcao[0] == "3":
            print("Saindo do programa...")
        else:
            print("Opção inválida. Tente novamente.")
            
            
if __name__ == "__main__":
    menu()
