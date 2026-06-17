from datetime import datetime
from utils import (cab, pausar, msg_sucesso, msg_erro, msg_aviso,
                   proximo_id, listar_todos, salvar_todos, buscar_por_cpf,
                   CYAN, BOLD, RESET, WHITE, DIM, YELLOW)

def cadastrar():
    cab()
    print(CYAN + BOLD + "  [ CADASTRAR CLIENTE ]\n" + RESET)

    nome = input(WHITE + "  Nome completo : " + RESET).strip()
    if not nome:
        msg_erro("Nome não pode ser vazio.")
        pausar(); return

    cidade = input(WHITE + "  Cidade        : " + RESET).strip()
    if not cidade:
        msg_erro("Cidade não pode ser vazia.")
        pausar(); return

    estado = input(WHITE + "  Estado (UF)   : " + RESET).strip().upper()
    if len(estado) != 2:
        msg_erro("Estado deve ter 2 letras (ex: GO, SP).")
        pausar(); return

    print(WHITE + "\n  Tipo de pessoa:" + RESET)
    print(DIM + "    [F] Pessoa Física   [J] Pessoa Jurídica" + RESET)
    tipo = input(WHITE + "  Escolha        : " + RESET).strip().upper()
    if tipo not in ("F", "J"):
        msg_erro("Tipo inválido. Use F ou J.")
        pausar(); return

    doc_label = "CPF" if tipo == "F" else "CNPJ"
    cpf_cnpj = input(WHITE + f"  {doc_label:<14}: " + RESET).strip()
    if not cpf_cnpj:
        msg_erro(f"{doc_label} não pode ser vazio.")
        pausar(); return

    if buscar_por_cpf(cpf_cnpj):
        msg_aviso(f"Já existe um cliente com este {doc_label}.")
        pausar(); return

    novo = {
        "id":            str(proximo_id()),
        "nome":          nome,
        "cidade":        cidade,
        "estado":        estado,
        "tipo":          tipo,
        "cpf_cnpj":      cpf_cnpj,
        "data_cadastro": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }

    clientes = listar_todos()
    clientes.append(novo)
    salvar_todos(clientes)

    msg_sucesso(f"Cliente '{nome}' cadastrado com ID {novo['id']}!")
    pausar()