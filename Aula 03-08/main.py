from tkinter import *
from tkinter import ttk

try:
    root = Tk()
    frm = ttk.Frame(root, padding=50)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Sair", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
except TclError:
    print("Hello World!")
    print("Pressione Enter para sair...")
    input()