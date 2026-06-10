import os

from datetime import datetime

def gerar_codigo():
    """Gera um código unico baseado na data e hora atual.
    Exemplo: CLI20240610123045
    """

    return "CLI" + datetime.now().strftime("%Y%m%d%H%M%S")


def cadastrar():
    os.system("cls" if os.name == "nt" else "clear")
    print("== CADASTRO DE CLIENTES ==")

    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    endereco = input("Endereço: ").strip()
    cidade = input("Cidade: ").strip()
    estado = input("Estado: ").strip()

    codigo = gerar_codigo()
    cliente = {
        "codigo": codigo,
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
        "cidade": cidade,
        "estado": estado
    }
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(str(cliente) + "\n")

    print(f"Cliente cadastrado com sucesso! Código: {codigo}")
    input("Pressione Enter para continuar...")




