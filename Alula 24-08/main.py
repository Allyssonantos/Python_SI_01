import tkinter as tk
from tkinter import ttk, messagebox

# 1º Passo: Configuração da Janela Principal (Tela)
janela = tk.Tk()
janela.title("Tkinter - Sistema de Cadastro")
janela.geometry("850x620")
janela.configure(bg="#e8e8e8")

# --- Barra de Menus ---
barra_menu = tk.Menu(janela)
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
menu_arquivo.add_command(label="Novo")
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=janela.quit)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

menu_ajuda = tk.Menu(barra_menu, tearoff=0)
menu_ajuda.add_command(label="Sobre", command=lambda: messagebox.showinfo("Sobre", "Sistema de Cadastro em Tkinter"))
barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)

janela.config(menu=barra_menu)

# --- Cabeçalho ---
header = tk.Frame(janela, bg="#2c3e50", height=45)
header.pack(fill="x", side="top")
lbl_titulo = tk.Label(
    header, 
    text="SISTEMA DE CADASTRO", 
    font=("Arial", 14, "bold"), 
    fg="white", 
    bg="#2c3e50"
)
lbl_titulo.pack(pady=8)

# Container Principal (para acomodar as colunas esquerda e direita)
frame_central = tk.Frame(janela, bg="#e8e8e8")
frame_central.pack(fill="both", expand=True, padx=10, pady=10)

# ==========================================
# 2º Passo: Frame Esquerdo - Dados Pessoais
# ==========================================
frame_dados = tk.LabelFrame(frame_central, text="Dados pessoais", font=("Arial", 10, "bold"), padx=10, pady=10)
frame_dados.pack(side="left", fill="both", expand=True, padx=(0, 5))

# 3º Passo: Elementos (Widgets) - Dados Pessoais
cadastros = []

# Nome
tk.Label(frame_dados, text="Nome:").grid(row=0, column=0, sticky="w", pady=2)
ent_nome = tk.Entry(frame_dados, width=30)
ent_nome.grid(row=0, column=1, columnspan=2, sticky="w", pady=2)

# Idade (Spinbox)
tk.Label(frame_dados, text="Idade:").grid(row=1, column=0, sticky="w", pady=2)
spn_idade = tk.Spinbox(frame_dados, from_=1, to=120, width=5)
spn_idade.grid(row=1, column=1, sticky="w", pady=2)

# Sexo (Radiobuttons)
tk.Label(frame_dados, text="Sexo:").grid(row=2, column=0, sticky="w", pady=2)
var_sexo = tk.StringVar(value="M")
tk.Radiobutton(frame_dados, text="Masculino", variable=var_sexo, value="M").grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame_dados, text="Feminino", variable=var_sexo, value="F").grid(row=2, column=2, sticky="w")

# Termos (Checkbutton)
var_termos = tk.BooleanVar()
chk_termos = tk.Checkbutton(frame_dados, text="Aceito os termos de cadastro", variable=var_termos)
chk_termos.grid(row=3, column=0, columnspan=3, sticky="w", pady=4)

# Linguagem (Combobox)
tk.Label(frame_dados, text="Linguagem:").grid(row=4, column=0, sticky="w", pady=2)
cb_linguagem = ttk.Combobox(frame_dados, values=["Python", "C++", "Java", "JavaScript", "PHP"], width=20)
cb_linguagem.current(0)
cb_linguagem.grid(row=4, column=1, columnspan=2, sticky="w", pady=2)

# Observações (Text)
tk.Label(frame_dados, text="Observações:").grid(row=5, column=0, sticky="nw", pady=2)
txt_obs = tk.Text(frame_dados, width=28, height=4)
txt_obs.grid(row=5, column=1, columnspan=2, sticky="w", pady=2)

# Disciplinas (Listbox)
tk.Label(frame_dados, text="Disciplinas:").grid(row=6, column=0, sticky="nw", pady=2)
lst_disciplinas = tk.Listbox(frame_dados, height=4, width=22)
for item in ["Banco de Dados", "Redes", "Programação Web", "Sistemas Operacionais"]:
    lst_disciplinas.insert(tk.END, item)
lst_disciplinas.grid(row=6, column=1, columnspan=2, sticky="w", pady=2)

# Botões de Ação
def abrir_nova_janela():
    nova = tk.Toplevel(janela)
    nova.title("Nova Janela")
    nova.geometry("300x150")
    tk.Label(nova, text="Janela secundária aberta!", font=("Arial", 11)).pack(expand=True)

def limpar_campos():
    ent_nome.delete(0, tk.END)
    txt_obs.delete("1.0", tk.END)
    spn_idade.delete(0, tk.END)
    spn_idade.insert(0, "1")
    var_termos.set(False)
    cb_linguagem.current(0)
    lst_disciplinas.selection_clear(0, tk.END)


def salvar_dados():
    nome = ent_nome.get().strip()
    if not nome:
        messagebox.showwarning("Cadastro", "Informe o nome antes de salvar.")
        ent_nome.focus()
        return

    if not var_termos.get():
        messagebox.showwarning("Cadastro", "Você precisa aceitar os termos antes de continuar.")
        return

    disciplinas = ", ".join(lst_disciplinas.get(i) for i in range(lst_disciplinas.size()) if lst_disciplinas.selection_includes(i))
    if not disciplinas:
        disciplinas = "Nenhuma disciplina selecionada"

    cadastro = {
        "nome": nome,
        "idade": spn_idade.get(),
        "sexo": var_sexo.get(),
        "linguagem": cb_linguagem.get(),
        "observacoes": txt_obs.get('1.0', tk.END).strip() or 'Nenhuma',
        "disciplinas": disciplinas,
    }
    cadastros.append(cadastro)
    lista_cadastros.insert(tk.END, f"{nome} - {spn_idade.get()} anos")

    mensagem = (
        f"Nome: {nome}\n"
        f"Idade: {spn_idade.get()}\n"
        f"Sexo: {var_sexo.get()}\n"
        f"Linguagem: {cb_linguagem.get()}\n"
        f"Observações: {cadastro['observacoes']}\n"
        f"Disciplinas: {disciplinas}"
    )

    messagebox.showinfo("Cadastro salvo", mensagem)
    limpar_campos()

frame_botoes = tk.Frame(frame_dados)
frame_botoes.grid(row=7, column=0, columnspan=3, pady=10)

btn_salvar = tk.Button(frame_botoes, text="Salvar", width=8, command=salvar_dados)
btn_salvar.pack(side="left", padx=3)

btn_limpar = tk.Button(frame_botoes, text="Limpar", width=8, command=limpar_campos)
btn_limpar.pack(side="left", padx=3)

btn_nova = tk.Button(frame_botoes, text="Nova Janela", width=10, command=abrir_nova_janela)
btn_nova.pack(side="left", padx=3)

# ==========================================
# 2º Passo: Frame Direito - Controles
# ==========================================
frame_controles = tk.LabelFrame(frame_central, text="Controles", font=("Arial", 10, "bold"), padx=10, pady=10)
frame_controles.pack(side="right", fill="both", expand=True, padx=(5, 0))

# 3º Passo: Elementos (Widgets) - Controles
# Scale (Slider)
tk.Label(frame_controles, text="Scale:").pack(anchor="w")
valor_scale = tk.IntVar(value=50)
scale = tk.Scale(frame_controles, from_=0, to=100, orient="horizontal", variable=valor_scale, command=lambda v: atualizar_canvas())
scale.set(50)
scale.pack(fill="x", pady=5)

# Canvas
def atualizar_canvas():
    valor = int(valor_scale.get())
    canvas.delete("all")
    canvas.create_line(15, 15, 265, 15, fill="black", width=2)

    largura = 30 + valor
    altura = 30 + valor // 2
    x1 = 30
    y1 = 30
    x2 = x1 + largura
    y2 = y1 + altura
    canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)

    raio = 25 + valor // 3
    x3 = 150
    y3 = 30
    x4 = x3 + raio * 2
    y4 = y3 + raio * 2
    canvas.create_oval(x3, y3, x4, y4, outline="black", width=2)

    canvas.create_text(140, 100, text=f"Valor: {valor}", font=("Arial", 8))


tk.Label(frame_controles, text="Canvas:").pack(anchor="w", pady=(5, 0))
canvas = tk.Canvas(frame_controles, width=280, height=110, bg="white", highlightthickness=1, highlightbackground="#ccc")
canvas.pack(pady=5)

atualizar_canvas()

# Message
msg = tk.Message(
    frame_controles, 
    text="O widget Message permite apresentar textos maiores com a quebra automática das linhas.", 
    width=260,
    font=("Arial", 8, "italic")
)
msg.pack(pady=10)

# Lista de cadastros consultados
ltk_label = tk.Label(frame_controles, text="Cadastros:", font=("Arial", 9, "bold"))
ltk_label.pack(anchor="w")
lista_cadastros = tk.Listbox(frame_controles, width=35, height=7)
lista_cadastros.pack(fill="x", pady=(5, 0))

# ==========================================
# Seção Inferior: Exemplo com place()
# ==========================================
frame_place = tk.LabelFrame(janela, text="Exemplo de PLACE", font=("Arial", 10, "bold"), height=70)
frame_place.pack(fill="x", padx=10, pady=(0, 10))

ent_place = tk.Entry(frame_place, width=20)
ent_place.place(x=10, y=10)

btn_ok = tk.Button(frame_place, text="OK", width=6)
btn_ok.place(x=180, y=8)

# Posicionamento relativo com place()
btn_relativo = tk.Button(frame_place, text="Botão relativo")
btn_relativo.place(relx=0.6, rely=0.15, relwidth=0.3, height=25)

# Loop da aplicação
janela.mainloop()