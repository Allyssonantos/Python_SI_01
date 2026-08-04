from pathlib import Path
import json

ARQUIVO = Path(__file__).with_name("clientes.txt")


def _carregar_clientes():
    if not ARQUIVO.exists():
        return []

    texto = ARQUIVO.read_text(encoding="utf-8").strip()
    if not texto:
        return []

    try:
        dados = json.loads(texto)
        if isinstance(dados, list):
            return dados
    except json.JSONDecodeError:
        return []

    return []


def listar_todos():
    return _carregar_clientes()


def consultar_gui(cpf):
    cpf = (cpf or "").strip()
    clientes = _carregar_clientes()

    if not cpf:
        return clientes

    for cliente in clientes:
        if cliente.get("cpf") == cpf:
            return cliente

    return None


def consultar():
    print("\n=== CONSULTA DE CLIENTE ===")
    cpf = input("Digite o CPF para consultar: ").strip()
    clientes = _carregar_clientes()

    for cliente in clientes:
        if cliente.get("cpf") == cpf:
            print("\nCliente encontrado:")
            print(f"Nome: {cliente.get('nome')}")
            print(f"CPF: {cliente.get('cpf')}")
            print(f"Cidade: {cliente.get('cidade')}")
            print(f"Estado: {cliente.get('estado')}")
            input("\nPressione Enter para continuar...")
            return

    print("Cliente não encontrado.")
    input("\nPressione Enter para continuar...")
