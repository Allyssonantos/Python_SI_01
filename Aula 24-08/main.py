import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Sistema de Cadastro")
janela.geometry("850x620")
janela.resizable(whidth=False, height=False)


frame1 = tk.Frame(janela)
frame1.grid(row=0, column=0)

frame2 = tk.Frame(janela)
frame2.grid(row=0, column=1)

botao1 = tk.Button(frame1, text="Botão 1", width=25, height=2)
botao1.pack(pady=5)

botao2= tk.Button(frame1, text="Cadastro", width=25, height=2)
botao2.pack(pady=5)