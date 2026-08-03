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

#== Dupla: Allysson, Carlos Henrique Gomes dos Santos ==

import os
import cadastro
import consulta
import alteracao
import exclusao


while True:
    # Limpa a tela a cada vez que o menu é exibido
    os.system("cls" if os.name == "nt" else "clear")

    print("== SISTEMA DE CLIENTES ==\n")
    print("1 - Cadastrar Cliente")
    print("2 - Consultar Cliente")
    print("3 - Alterar Cliente")
    print("4 - Excluir Cliente")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()

    # Chama o módulo correspondente à opção escolhida
    if opcao == "1":
        cadastro.cadastrar()
    elif opcao == "2":
        consulta.consultar()
    elif opcao == "3":
        alteracao.alterar()
    elif opcao == "4":
        exclusao.excluir()
    elif opcao == "5":
        print("\nAté logo!")
        break
    else:
        print("Opção inválida.")
        input("\nPressione Enter para continuar...")

  