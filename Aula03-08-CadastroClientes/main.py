from tkinter import Tk, Toplevel, ttk, StringVar
from tkinter import TclError
from tkinter.messagebox import showinfo, showerror

import cadastro
import consulta
import alteracao
import exclusao


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
    janela.geometry("420x260")

    frame = ttk.Frame(janela, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="CPF para consultar (deixe vazio para listar todos):").pack(anchor="w")
    cpf = StringVar()
    ttk.Entry(frame, textvariable=cpf).pack(fill="x", pady=(0, 10))

    def buscar():
        try:
            resultado = consulta.consultar_gui(cpf.get())
            showinfo("Resultado", resultado)
            janela.destroy()
        except Exception as exc:
            showerror("Erro", f"Erro ao consultar: {exc}")

    ttk.Button(frame, text="Consultar", command=buscar).pack()


def abrir_alteracao(root):
    janela = Toplevel(root)
    janela.title("Alteração")
    janela.geometry("320x300")

    frame = ttk.Frame(janela, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="CPF do cliente:").pack(anchor="w")
    cpf = StringVar()
    ttk.Entry(frame, textvariable=cpf).pack(fill="x", pady=(0, 8))
    ttk.Label(frame, text="Novo nome:").pack(anchor="w")
    nome = StringVar()
    ttk.Entry(frame, textvariable=nome).pack(fill="x", pady=(0, 8))
    ttk.Label(frame, text="Nova cidade:").pack(anchor="w")
    cidade = StringVar()
    ttk.Entry(frame, textvariable=cidade).pack(fill="x", pady=(0, 8))
    ttk.Label(frame, text="Novo estado:").pack(anchor="w")
    estado = StringVar()
    ttk.Entry(frame, textvariable=estado).pack(fill="x", pady=(0, 8))

    def alterar():
        try:
            mensagem = alteracao.alterar_gui(cpf.get(), nome.get(), cidade.get(), estado.get())
            showinfo("Sucesso", mensagem)
            janela.destroy()
        except Exception as exc:
            showerror("Erro", f"Erro ao alterar: {exc}")

    ttk.Button(frame, text="Alterar", command=alterar).pack()


def abrir_exclusao(root):
    janela = Toplevel(root)
    janela.title("Exclusão")
    janela.geometry("300x160")

    frame = ttk.Frame(janela, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="CPF para excluir:").pack(anchor="w")
    cpf = StringVar()
    ttk.Entry(frame, textvariable=cpf).pack(fill="x", pady=(0, 10))

    def remover():
        try:
            mensagem = exclusao.excluir_gui(cpf.get())
            showinfo("Resultado", mensagem)
            janela.destroy()
        except Exception as exc:
            showerror("Erro", f"Erro ao excluir: {exc}")

    ttk.Button(frame, text="Excluir", command=remover).pack()


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
  