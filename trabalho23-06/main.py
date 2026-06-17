#Trabalho em Dupla
#Data da entrega 23/06
#Faça um programa em Python e poste aqui todos os módulos
#O Programa é um Controle de clientes com:
#- Menu com opções  
#- Cadastro
#- Consulta (por cpf)
#- Listagem
#- Alteração
#- Exclusão
#Os dados devem ser gravados em arquivo de texto e são: id, nome, cidade, estado, tipo, cpf/cnpj e data de cadastro
#Consulta, alteração, exclusão devem ser pesquisado por cpf ou cnpj

import os
import cadastro
import consulta
import exclusao


while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("== SISTEMA DE CLIENTES ==\n")
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
        print("\nAté logo!")
        break
    else:
        print("Opção inválida.")
        input("\nPressione Enter para continuar...")

  