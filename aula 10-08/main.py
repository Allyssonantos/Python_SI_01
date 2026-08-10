import tkinter as tk

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("800x600")

frame_titulo = tk.Frame(janela)
frame_titulo.pack(fill= "x", padx=10, pady=10)

tk.Label(frame_titulo, text="Cadastro de Clientes", font=("Arial", 20)).pack()
tk.Label(frame_titulo, text="Preencha os campos abaixo para cadastrar um novo cliente.", font=("Arial", 12)).pack()

frame_form = tk.Frame(janela)
frame_form.pack(fill="both", padx=10, pady=10)

tk.Label(frame_form, text="Código:").grid(row=0, column=0, sticky="w", padx=5, pady=5)

tk.Entry(frame_form).grid(row=0, column=1, padx=5, pady=5) 

janela.mainloop()   