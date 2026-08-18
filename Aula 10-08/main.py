from tkinter import Tk, Toplevel, ttk, StringVar
from tkinter import TclError
from tkinter.messagebox import showinfo, showerror

import cadastro
import consulta
import alteracao
import exclusao

def salvar():
    nome.delete(0, tk.END)
    telefone.delete(0, tk.END)
    email.delete(0, tk.END)
    cidade.delete(0, tk.END)
    estado.delete(0, tk.END)
    tipo.delete(0, tk.END)
    documento.delete(0, tk.END)
    nome.focus()


tk.Label (frame_form, text="Tipo (CNPJ ou CPF):").pack(pady = 2)
tipo = tk.Entry (frame_form, width=30)
tipo.pack(pady = 2)


tk.Label (frame_form, text="Documento:").pack(pady = 2)
documento = tk.Entry (frame_form, width=30)
documento.pack(pady = 2)

botao1 = tk.Button (janela, text="Salvar", command=salvar).pack(pady = 15)
botao1.pack(pady = 15)

nome.focus()

nome.bind("<Return>", lambda event: telefone.focus())
telefone.bind("<Return>", lambda event: email.focus())
email.bind("<Return>", lambda event: cidade.focus())
cidade.bind("<Return>", lambda event: estado.focus())
estado.bind("<Return>", lambda event: tipo.focus())
tipo.bind("<Return>", lambda event: documento.focus())
documento.bind("<Return>", lambda event: botao1.focus())