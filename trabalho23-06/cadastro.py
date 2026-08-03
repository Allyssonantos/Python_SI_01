import os
import ast
from datetime import datetime


def gerar_codigo():
    # Gera um código único baseado na data e hora atual
    # Exemplo: CLI20240610123045
    return "CLI" + datetime.now().strftime("%Y%m%d%H%M%S")


def cadastrar():
    os.system("cls" if os.name == "nt" else "clear")
    print("== CADASTRO DE CLIENTES ==\n")

    # Coleta os dados do cliente pelo teclado
    nome     = input("Nome: ").strip()
    cpf      = input("CPF: ").strip()
    telefone = input("Telefone: ").strip()
    email    = input("E-mail: ").strip()
    endereco = input("Endereço: ").strip()
    cidade   = input("Cidade: ").strip()
    estado   = input("Estado: ").strip()

    # Gera o código único para o cliente
    codigo = gerar_codigo()

    # Cria o dicionário com todos os dados do cliente
    cliente = {
        "codigo": codigo, "nome": nome, "cpf": cpf,
        "telefone": telefone, "email": email,
        "endereco": endereco, "cidade": cidade, "estado": estado
    }

    # Salva o cliente no arquivo de texto
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(str(cliente) + "\n")

    print(f"\nCliente cadastrado com sucesso! Código: {codigo}")
    input("\nPressione Enter para continuar...")