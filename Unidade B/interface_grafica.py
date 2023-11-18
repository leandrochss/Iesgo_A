import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Olá, IESGO!")

def fechar_janela():
    resposta = messagebox.askokcancel("Fechar Janela", "Tem certeza que deseja fechar a janela?")
    if resposta:
        janela.destroy()

def alterar_rotulo():
    novo_texto = entrada.get()
    label.config(text=f"Novo texto: {novo_texto}")

# criar uma janela
janela = tk.Tk()
janela.title("Exemplo de GUI em Python")

# criar um rótulo
label = tk.Label(janela, text="Bem-vindo à interface gráfica de usuário")
label.pack(padx=10, pady=10)
label.config(width=50, height=5)

# criar um botão do tipo CTA (call to action)
botao = tk.Button(janela, text="Mostrar Mensagem", command=mostrar_mensagem)
botao.pack(side=tk.LEFT, padx=10, pady=10)
botao.config(width=15, height=2)

# criar um botão para fechar a janela
botao_fechar = tk.Button(janela, text="Fechar Janela", command=fechar_janela)
botao_fechar.pack(side=tk.RIGHT, padx=5, pady=5)
botao_fechar.config(width=15, height=2)

# criar uma entrada de texto
entrada = tk.Entry(janela, width=30)
entrada.pack(pady=10)

# criar um botão para alterar o rótulo com base no texto da entrada
botao_alterar_rotulo = tk.Button(janela, text="Alterar Rótulo", command=alterar_rotulo)
botao_alterar_rotulo.pack(pady=5)

# iniciar a GUI em loop
janela.mainloop()
