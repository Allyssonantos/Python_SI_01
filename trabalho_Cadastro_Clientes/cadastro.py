from pathlib import Path
import json

ARQUIVO = Path(__file__).with_name("clientes.txt")


def _carregar_clientes():
    if not ARQUIVO.exists():
        ARQUIVO.write_text("[]", encoding="utf-8")
        return []

    texto = ARQUIVO.read_text(encoding="utf-8").strip()
    if not texto:
        return []

    try:
        dados = json.loads(texto)
        if isinstance(dados, list):
            return dados
    except json.JSONDecodeError:
        pass

    return []


def _salvar_clientes(clientes):
    ARQUIVO.write_text(json.dumps(clientes, ensure_ascii=False, indent=2), encoding="utf-8")


def cadastrar_gui(nome, cpf, cidade, estado):
    nome = (nome or "").strip()
    cpf = (cpf or "").strip()
    cidade = (cidade or "").strip()
    estado = (estado or "").strip().upper()

    if not nome or not cpf or not cidade or not estado:
        raise ValueError("Todos os campos devem ser preenchidos.")

    clientes = _carregar_clientes()
    clientes.append({
        "nome": nome,
        "cpf": cpf,
        "cidade": cidade,
        "estado": estado,
    })
    _salvar_clientes(clientes)
    return True


def cadastrar():
    print("\n=== CADASTRO DE CLIENTE ===")
    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()
    cidade = input("Cidade: ").strip()
    estado = input("Estado: ").strip().upper()

    clientes = _carregar_clientes()
    clientes.append({
        "nome": nome,
        "cpf": cpf,
        "cidade": cidade,
        "estado": estado,
    })
    _salvar_clientes(clientes)

    print("\nCliente cadastrado com sucesso!")
    input("\nPressione Enter para continuar...")
