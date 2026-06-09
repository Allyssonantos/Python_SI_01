





def gerar_codigo():
    """Gera um código unico baseado na data e hora atual.
    Exemplo: CLI20240610123045
    """

    return "CLI" + datetime.now().strftime("%Y%m%d%H%M%S")


def cadastrar()
    os.system("clear")
    print("== CADASTRO DE CLIENTES ==")

    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    endereco = input("Endereço: ").strip()
    cidade = input("Cidade: ").strip()
    estado = input("Estado: ").strip()

    codigo = gerar_codigo()

    