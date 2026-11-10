import os
import cadastro
import consulta
import exclusao

# ── Cores ANSI ──────────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
WHITE  = "\033[97m"
DIM    = "\033[2m"

# ── Caracteres de borda ──────────────────────────────────────
TL, TR, BL, BR = "╔", "╗", "╚", "╝"
H, V           = "═", "║"
ML, MR         = "╠", "╣"

LARGURA = 36


def linha_topo():
    return CYAN + TL + H * LARGURA + TR + RESET

def linha_fundo():
    return CYAN + BL + H * LARGURA + BR + RESET

def linha_divisor():
    return CYAN + ML + H * LARGURA + MR + RESET

def linha_vazia():
    return CYAN + V + " " * LARGURA + V + RESET

def linha_texto(texto, cor="", centralizado=True):
    if centralizado:
        visivel = len(texto)
        pad = LARGURA - visivel
        esq = pad // 2
        dir = pad - esq
        conteudo = " " * esq + cor + texto + RESET + " " * dir
    else:
        visivel = len(texto)
        conteudo = " " + cor + texto + RESET + " " * (LARGURA - visivel - 1)
    return CYAN + V + RESET + conteudo + CYAN + V + RESET

def linha_opcao(num, texto):
    entrada = f"  {num}  {texto}"
    visivel = len(entrada)
    conteudo = YELLOW + f"  {num}" + RESET + f"  {texto}" + " " * (LARGURA - visivel)
    return CYAN + V + RESET + conteudo + CYAN + V + RESET


def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print()
        print(linha_topo())
        print(linha_vazia())
        print(linha_texto("SISTEMA DE CLIENTES", BOLD + WHITE))
        print(linha_vazia())
        print(linha_divisor())
        print(linha_vazia())
        print(linha_opcao("1", "Cadastrar Cliente"))
        print(linha_vazia())
        print(linha_opcao("2", "Consultar Cliente"))
        print(linha_vazia())
        print(linha_opcao("3", "Excluir Cliente"))
        print(linha_vazia())
        print(linha_opcao("4", "Sair"))
        print(linha_vazia())
        print(linha_fundo())
        print()

        opcao = input(CYAN + "  >> " + RESET).strip()

        if opcao == "1":
            cadastro.cadastrar()
        elif opcao == "2":
            consulta.consultar()
        elif opcao == "3":
            exclusao.excluir()
        elif opcao == "4":
            os.system("cls" if os.name == "nt" else "clear")
            print()
            print(linha_topo())
            print(linha_vazia())
            print(linha_texto("Até logo!", BOLD + GREEN))
            print(linha_vazia())
            print(linha_fundo())
            print()
            break
        else:
            print(RED + "  Opção inválida. Tente novamente." + RESET)
            input(DIM + "  Pressione Enter para continuar..." + RESET)


if __name__ == "__main__":
    menu()