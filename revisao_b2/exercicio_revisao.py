import sqlite3

# Função para criar o banco de dados e a tabela
def criar_banco():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Criar tabela livros se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            ano_publicacao INTEGER
        )
    ''')

    conn.commit()
    conn.close()

# Função para inserir um livro
def inserir_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_publicacao = int(input("Digite o ano de publicação do livro: "))

    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Inserir livro na tabela
    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano_publicacao)
        VALUES (?, ?, ?)
    ''', (titulo, autor, ano_publicacao))

    conn.commit()
    conn.close()

# Função para consultar todos os livros
def consultar_livros():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Selecionar todos os livros
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()

    # Exibir todos os livros
    for livro in livros:
        print(livro)

    conn.close()

# Função para remover um livro
def remover_livro():
    id_livro = int(input("Digite o ID do livro que deseja remover: "))

    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Remover livro da tabela
    cursor.execute('DELETE FROM livros WHERE id = ?', (id_livro,))

    conn.commit()
    conn.close()

# Função principal
def main():
    criar_banco()

    while True:
        print("\n=== Menu ===")
        print("1. Inserir livro")
        print("2. Consultar todos os livros")
        print("3. Remover livro")
        print("4. Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == '1':
            inserir_livro()
        elif opcao == '2':
            consultar_livros()
        elif opcao == '3':
            remover_livro()
        elif opcao == '4':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
