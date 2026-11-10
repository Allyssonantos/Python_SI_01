from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculadora")

resultado = StringVar()

entry = ttk.Entry(root, textvariable=resultado, width=20, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Variável para guardar a operação que está sendo montada
expressao = ""


def adicionar(valor):
    global expressao
    expressao += str(valor)
    resultado.set(expressao)


def limpar():
    global expressao
    expressao = ""
    resultado.set("")


def calcular():
    global expressao
    try:
        valor = eval(expressao)
        resultado.set(str(valor))
        expressao = str(valor)
    except Exception:
        resultado.set("Erro")
        expressao = ""


# Botões numéricos
numeros = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for texto, linha, coluna in numeros:
    comando = None
    if texto == "=":
        comando = calcular
    elif texto == ".":
        comando = lambda txt=texto: adicionar(txt)
    elif texto in "+-*/":
        comando = lambda txt=texto: adicionar(txt)
    else:
        comando = lambda txt=texto: adicionar(txt)

    ttk.Button(root, text=texto, command=comando, width=4).grid(row=linha, column=coluna, padx=5, pady=5)

# Botão limpar
btn_limpar = ttk.Button(root, text="C", command=limpar, width=4)
btn_limpar.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Botão sair
btn_sair = ttk.Button(root, text="Sair", command=root.destroy, width=6)
btn_sair.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()