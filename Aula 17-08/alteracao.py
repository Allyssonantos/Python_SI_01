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


def alterar_gui(cpf, nome, cidade, estado):
    if not cpf.strip():
        raise ValueError("CPF é obrigatório.")

    clientes = _carregar_clientes()
    for cliente in clientes:
        if cliente.get("cpf") == cpf.strip():
            cliente["nome"] = nome.strip() or cliente.get("nome")
            cliente["cidade"] = cidade.strip() or cliente.get("cidade")
            cliente["estado"] = estado.strip().upper() or cliente.get("estado")
            _salvar_clientes(clientes)
            return "Cliente alterado com sucesso!"

    return "Cliente não encontrado."


def alterar():
    print("\n=== ALTERAÇÃO DE CLIENTE ===")
    cpf = input("Digite o CPF do cliente a alterar: ").strip()
    clientes = _carregar_clientes()

    for cliente in clientes:
        if cliente.get("cpf") == cpf:
            cliente["nome"] = input("Novo nome: ").strip() or cliente.get("nome")
            cliente["cidade"] = input("Nova cidade: ").strip() or cliente.get("cidade")
            cliente["estado"] = input("Novo estado: ").strip().upper() or cliente.get("estado")
            _salvar_clientes(clientes)
            print("\nCliente alterado com sucesso!")
            input("\nPressione Enter para continuar...")
            return

    print("Cliente não encontrado.")
    input("\nPressione Enter para continuar...")
