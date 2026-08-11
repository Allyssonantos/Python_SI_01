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


def _salvar_clientes(clientes):
    ARQUIVO.write_text(json.dumps(clientes, ensure_ascii=False, indent=2), encoding="utf-8")


def excluir_gui(cpf):
    if not cpf.strip():
        raise ValueError("CPF é obrigatório.")

    clientes = _carregar_clientes()
    novos_clientes = [cliente for cliente in clientes if cliente.get("cpf") != cpf.strip()]

    if len(novos_clientes) == len(clientes):
        return "Cliente não encontrado."

    _salvar_clientes(novos_clientes)
    return "Cliente excluído com sucesso!"


def excluir():
    print("\n=== EXCLUSÃO DE CLIENTE ===")
    cpf = input("Digite o CPF do cliente a excluir: ").strip()
    clientes = _carregar_clientes()
    novos_clientes = [cliente for cliente in clientes if cliente.get("cpf") != cpf]

    if len(novos_clientes) == len(clientes):
        print("Cliente não encontrado.")
    else:
        _salvar_clientes(novos_clientes)
        print("Cliente excluído com sucesso!")

    input("\nPressione Enter para continuar...")
