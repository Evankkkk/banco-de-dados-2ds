import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

# Criação da tabela de clientes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
""")

conexao.commit()


# Função para salvar os dados do cliente
def salvar_cliente():
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    # Validação dos campos
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos antes de salvar!"
        )
        return

    try:
        cursor.execute(
            "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
            (nome, email, telefone)
        )

        conexao.commit()

        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )

        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível salvar o cliente: {erro}"
        )


# Função para limpar o formulário
def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_nome.focus()


# Função para fechar a conexão ao encerrar
def fechar_programa():
    conexao.close()
    janela.destroy()


# Criação da janela principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("400x350")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="FORMULÁRIO DE CADASTRO",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=20)

# Campo Nome
tk.Label(janela, text="Nome:", font=("Arial", 11)).pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack(pady=5)

# Campo E-mail
tk.Label(janela, text="E-mail:", font=("Arial", 11)).pack()
entrada_email = tk.Entry(janela, width=40)
entrada_email.pack(pady=5)

# Campo Telefone
tk.Label(janela, text="Telefone:", font=("Arial", 11)).pack()
entrada_telefone = tk.Entry(janela, width=40)
entrada_telefone.pack(pady=5)

# Botão Salvar
botao_salvar = tk.Button(
    janela,
    text="Salvar Cliente",
    command=salvar_cliente,
    bg="green",
    fg="white",
    width=20
)
botao_salvar.pack(pady=10)

# Botão Limpar
botao_limpar = tk.Button(
    janela,
    text="Limpar Formulário",
    command=limpar_formulario,
    width=20
)
botao_limpar.pack(pady=5)

# Evento de fechamento da janela
janela.protocol("WM_DELETE_WINDOW", fechar_programa)

# Iniciar a interface gráfica
entrada_nome.focus()
janela.mainloop()


import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

# Criação da tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
""")

conexao.commit()


# Função para salvar cliente
def salvar_cliente():
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos!"
        )
        return

    try:
        cursor.execute("""
            INSERT INTO clientes (nome, email, telefone)
            VALUES (?, ?, ?)
        """, (nome, email, telefone))

        conexao.commit()

        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )

        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror("Erro", str(erro))


# Função para limpar formulário
def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_nome.focus()


# NOVA FUNCIONALIDADE: Visualizar clientes
def visualizar_clientes():
    janela_clientes = tk.Toplevel(janela)
    janela_clientes.title("Clientes Cadastrados")
    janela_clientes.geometry("700x400")
    janela_clientes.resizable(True, True)

    titulo_lista = tk.Label(
        janela_clientes,
        text="LISTA DE CLIENTES CADASTRADOS",
        font=("Arial", 14, "bold")
    )
    titulo_lista.pack(pady=15)

    # Criação da tabela
    colunas = ("ID", "Nome", "E-mail", "Telefone")

    tabela = ttk.Treeview(
        janela_clientes,
        columns=colunas,
        show="headings"
    )

    tabela.heading("ID", text="ID")
    tabela.heading("Nome", text="Nome")
    tabela.heading("E-mail", text="E-mail")
    tabela.heading("Telefone", text="Telefone")

    tabela.column("ID", width=50, anchor="center")
    tabela.column("Nome", width=180)
    tabela.column("E-mail", width=220)
    tabela.column("Telefone", width=150)

    tabela.pack(fill="both", expand=True, padx=10, pady=10)

    # Barra de rolagem
    scrollbar = ttk.Scrollbar(
        janela_clientes,
        orient="vertical",
        command=tabela.yview
    )
    tabela.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    try:
        cursor.execute("""
            SELECT id, nome, email, telefone
            FROM clientes
            ORDER BY id
        """)

        clientes = cursor.fetchall()

        if clientes:
            for cliente in clientes:
                tabela.insert("", tk.END, values=cliente)
        else:
            messagebox.showinfo(
                "Informação",
                "Nenhum cliente cadastrado.",
                parent=janela_clientes
            )

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Erro ao consultar clientes: {erro}",
            parent=janela_clientes
        )


# Função para fechar o programa
def fechar_programa():
    conexao.close()
    janela.destroy()


# Criação da janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro de Clientes")
janela.geometry("420x420")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="CADASTRO DE CLIENTES",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=20)

# Campo Nome
tk.Label(janela, text="Nome:").pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack(pady=5)

# Campo E-mail
tk.Label(janela, text="E-mail:").pack()
entrada_email = tk.Entry(janela, width=40)
entrada_email.pack(pady=5)

# Campo Telefone
tk.Label(janela, text="Telefone:").pack()
entrada_telefone = tk.Entry(janela, width=40)
entrada_telefone.pack(pady=5)

# Botão Salvar
tk.Button(
    janela,
    text="Salvar Cliente",
    command=salvar_cliente,
    bg="green",
    fg="white",
    width=25
).pack(pady=10)

# Botão Limpar
tk.Button(
    janela,
    text="Limpar Formulário",
    command=limpar_formulario,
    width=25
).pack(pady=5)

# NOVO BOTÃO: Visualizar Clientes
tk.Button(
    janela,
    text="Visualizar Clientes",
    command=visualizar_clientes,
    bg="blue",
    fg="white",
    width=25
).pack(pady=5)

# Fechamento do programa
janela.protocol("WM_DELETE_WINDOW", fechar_programa)

entrada_nome.focus()

# Iniciar programa
janela.mainloop()
