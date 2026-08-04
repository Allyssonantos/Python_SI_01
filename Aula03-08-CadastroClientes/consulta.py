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


def consultar_gui(cpf):
    cpf = (cpf or "").strip()
    clientes = _carregar_clientes()

    if not cpf:
        if not clientes:
            return "Nenhum cliente cadastrado."

        lista = []
        for cliente in clientes:
            lista.append(
                f"Nome: {cliente.get('nome')} | CPF: {cliente.get('cpf')} | "
                f"Cidade: {cliente.get('cidade')} | Estado: {cliente.get('estado')}"
            )
        return "\n".join(lista)

    for cliente in clientes:
        if cliente.get("cpf") == cpf:
            return (
                f"Cliente encontrado:\n"
                f"Nome: {cliente.get('nome')}\n"
                f"CPF: {cliente.get('cpf')}\n"
                f"Cidade: {cliente.get('cidade')}\n"
                f"Estado: {cliente.get('estado')}"
            )

    return "Cliente não encontrado."


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
