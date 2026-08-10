import tkinter as tk
from tkinter import Tk, Toplevel, ttk, StringVar
from tkinter import TclError
from tkinter.messagebox import showinfo, showerror

import cadastro
import consulta
import alteracao
import exclusao

def _criar_tree_clientes(frame, height=10):
    container = ttk.Frame(frame)
    tree = ttk.Treeview(
        container,
        columns=("nome", "cpf", "cidade", "estado"),
        show="headings",
        height=height,
        selectmode="browse",
    )
    tree.heading("nome", text="Nome")
    tree.heading("cpf", text="CPF")
    tree.heading("cidade", text="Cidade")
    tree.heading("estado", text="Estado")
    tree.column("nome", width=160)
    tree.column("cpf", width=120)
    tree.column("cidade", width=160)
    tree.column("estado", width=100)

    y_scroll = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
    x_scroll = ttk.Scrollbar(container, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    tree.grid(row=0, column=0, sticky="nsew")
    y_scroll.grid(row=0, column=1, sticky="ns")
    x_scroll.grid(row=1, column=0, sticky="ew")
    container.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    return container, tree


def _popular_tree_clientes(tree, clientes):
    for item in tree.get_children():
        tree.delete(item)

    for cliente in clientes:
        tree.insert(
            "",
            "end",
            values=(
                cliente.get("nome", ""),
                cliente.get("cpf", ""),
                cliente.get("cidade", ""),
                cliente.get("estado", ""),
            ),
        )


def abrir_cadastro(root):
    janela = Toplevel(root)
    janela.title("Cadastro")
    janela.geometry("320x280")

    frame = ttk.Frame(janela, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Cadastro de Cliente").pack(pady=8)
    nome = StringVar()
    cpf = StringVar()
    cidade = StringVar()
    estado = StringVar()

    ttk.Label(frame, text="Nome:").pack(anchor="w")
    ttk.Entry(frame, textvariable=nome).pack(fill="x", pady=(0, 6))
    ttk.Label(frame, text="CPF:").pack(anchor="w")
    ttk.Entry(frame, textvariable=cpf).pack(fill="x", pady=(0, 6))
    ttk.Label(frame, text="Cidade:").pack(anchor="w")
    ttk.Entry(frame, textvariable=cidade).pack(fill="x", pady=(0, 6))
    ttk.Label(frame, text="Estado:").pack(anchor="w")
    ttk.Entry(frame, textvariable=estado).pack(fill="x", pady=(0, 6))

    def salvar():
        try:
            cadastro.cadastrar_gui(nome.get(), cpf.get(), cidade.get(), estado.get())
            showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            janela.destroy()
        except Exception as exc:
            showerror("Erro", f"Erro ao cadastrar: {exc}")

    ttk.Button(frame, text="Salvar", command=salvar).pack(pady=10)


def abrir_consulta(root):
    janela = Toplevel(root)
    janela.title("Consulta")
    janela.geometry("700x360")

    frame = ttk.Frame(janela, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="CPF para consultar (deixe vazio para listar todos):").pack(anchor="w")
    cpf = StringVar()
    ttk.Entry(frame, textvariable=cpf).pack(fill="x", pady=(0, 10))

    ttk.Label(frame, text="Lista de clientes cadastrados").pack(anchor="w")
    container, tree = _criar_tree_clientes(frame, height=8)
    container.pack(fill="both", expand=True, pady=(0, 10))

    def carregar_tabela():
        filtro = cpf.get().strip()
        clientes = consulta.listar_todos()

        if filtro:
            clientes = [cliente for cliente in clientes if cliente.get("cpf") == filtro]

        if not clientes:
            showinfo("Resultado", "Nenhum cliente cadastrado.")
            _popular_tree_clientes(tree, [])
            return

        _popular_tree_clientes(tree, clientes)

    def buscar():
        try:
            carregar_tabela()
        except Exception as exc:
            showerror("Erro", f"Erro ao consultar: {exc}")

    ttk.Button(frame, text="Consultar", command=buscar).pack(side="left", padx=(0, 10))
    ttk.Button(frame, text="Listar todos", command=carregar_tabela).pack(side="left", padx=(0, 10))
    ttk.Button(frame, text="Limpar filtro", command=lambda: (cpf.set(""), carregar_tabela())).pack(side="left")


def abrir_alteracao(root):
    janela = Toplevel(root)
    janela.title("Alteração")
    janela.geometry("780x420")

    frame = ttk.Frame(janela, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Clientes cadastrados:").pack(anchor="w")
    container, tree = _criar_tree_clientes(frame, height=6)
    container.pack(fill="both", expand=True, pady=(0, 12))

    campos = ttk.Frame(frame)
    campos.pack(fill="x")

    ttk.Label(campos, text="CPF do cliente:").pack(anchor="w")
    cpf = StringVar()
    ttk.Entry(campos, textvariable=cpf).pack(fill="x", pady=(0, 8))
    ttk.Label(campos, text="Novo nome:").pack(anchor="w")
    nome = StringVar()
    ttk.Entry(campos, textvariable=nome).pack(fill="x", pady=(0, 8))
    ttk.Label(campos, text="Nova cidade:").pack(anchor="w")
    cidade = StringVar()
    ttk.Entry(campos, textvariable=cidade).pack(fill="x", pady=(0, 8))
    ttk.Label(campos, text="Novo estado:").pack(anchor="w")
    estado = StringVar()
    ttk.Entry(campos, textvariable=estado).pack(fill="x", pady=(0, 8))

    def preencher_campos(item):
        valores = tree.item(item, "values")
        if not valores:
            return

        cpf.set(valores[1])
        nome.set(valores[0])
        cidade.set(valores[2])
        estado.set(valores[3])

    def carregar_tabela():
        _popular_tree_clientes(tree, consulta.listar_todos())

    tree.bind("<<TreeviewSelect>>", lambda event: preencher_campos(tree.selection()[0]) if tree.selection() else None)

    def alterar():
        try:
            mensagem = alteracao.alterar_gui(cpf.get(), nome.get(), cidade.get(), estado.get())
            showinfo("Sucesso", mensagem)
            carregar_tabela()
        except Exception as exc:
            showerror("Erro", f"Erro ao alterar: {exc}")

    ttk.Button(frame, text="Alterar", command=alterar).pack(pady=(10, 0))
    carregar_tabela()


def abrir_exclusao(root):
    janela = Toplevel(root)
    janela.title("Exclusão")
    janela.geometry("780x420")

    frame = ttk.Frame(janela, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Clientes cadastrados:").pack(anchor="w")
    container, tree = _criar_tree_clientes(frame, height=6)
    container.pack(fill="both", expand=True, pady=(0, 12))

    ttk.Label(frame, text="CPF para excluir:").pack(anchor="w")
    cpf = StringVar()
    ttk.Entry(frame, textvariable=cpf).pack(fill="x", pady=(0, 10))

    def preencher_cpf(item):
        valores = tree.item(item, "values")
        if not valores:
            return
        cpf.set(valores[1])

    def carregar_tabela():
        _popular_tree_clientes(tree, consulta.listar_todos())

    tree.bind("<<TreeviewSelect>>", lambda event: preencher_cpf(tree.selection()[0]) if tree.selection() else None)

    def remover():
        try:
            mensagem = exclusao.excluir_gui(cpf.get())
            showinfo("Resultado", mensagem)
            carregar_tabela()
        except Exception as exc:
            showerror("Erro", f"Erro ao excluir: {exc}")

    ttk.Button(frame, text="Excluir", command=remover).pack()
    carregar_tabela()


try:
    root = Tk()
    root.title("Sistema de Clientes")
    root.geometry("420x300")

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="== SISTEMA DE CLIENTES ==", font=("Arial", 12, "bold")).pack(pady=(0, 12))

    ttk.Button(frame, text="Cadastrar Cliente", width=24, command=lambda: abrir_cadastro(root)).pack(pady=4)
    ttk.Button(frame, text="Consultar Cliente", width=24, command=lambda: abrir_consulta(root)).pack(pady=4)
    ttk.Button(frame, text="Alterar Cliente", width=24, command=lambda: abrir_alteracao(root)).pack(pady=4)
    ttk.Button(frame, text="Excluir Cliente", width=24, command=lambda: abrir_exclusao(root)).pack(pady=4)
    ttk.Button(frame, text="Sair", width=24, command=root.destroy).pack(pady=(8, 0))

    root.mainloop()
except TclError:
    print("Sistema de Clientes")
    print("Abra em uma máquina com interface gráfica para ver os botões.")
    raise SystemExit(0)
