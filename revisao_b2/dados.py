# Criar uma aplicação capaz de armazenar dados de usuários (nome, email, idade) via terminal. Crie um menu via terminal, permitindo add, remover via chave primária e visualizar a lista de usuários.
import sqlite3

# Função para criar o banco de dados e a tabela
def criar_banco():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    # Criar tabela usuarios se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            email TEXT PRIMARY KEY,
            nome TEXT,
            idade INTEGER
        )
    ''')

    conn.commit()
    conn.close()

# Função para adicionar um novo usuário
def adicionar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    idade = int(input("Digite a idade do usuário: "))

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    try:
        # Inserir usuário na tabela
        cursor.execute('''
            INSERT INTO usuarios (email, nome, idade)
            VALUES (?, ?, ?)
        ''', (email, nome, idade))
        print(f"Usuário {nome} adicionado com sucesso!")
    except sqlite3.IntegrityError:
        print("Usuário com o mesmo email já existe. Use outra chave primária.")

    conn.commit()
    conn.close()

# Função para remover um usuário por chave primária (email)
def remover_usuario():
    email = input("Digite o email do usuário que deseja remover: ")

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    # Remover usuário da tabela
    cursor.execute('DELETE FROM usuarios WHERE email = ?', (email,))

    if cursor.rowcount > 0:
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado.")

    conn.commit()
    conn.close()

# Função para visualizar a lista de usuários
def visualizar_usuarios():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    # Selecionar todos os usuários
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()

    print("\n=== Lista de Usuários ===")
    for usuario in usuarios:
        print(f"Email: {usuario[0]}")
        print(f"Nome: {usuario[1]}")
        print(f"Idade: {usuario[2]}")
        print("--------------------------")

    conn.close()

# Função principal
def main():
    criar_banco()

    while True:
        print("\n=== Menu ===")
        print("1. Adicionar Usuário")
        print("2. Remover Usuário por Chave Primária (email)")
        print("3. Visualizar Lista de Usuários")
        print("4. Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == '1':
            adicionar_usuario()
        elif opcao == '2':
            remover_usuario()
        elif opcao == '3':
            visualizar_usuarios()
        elif opcao == '4':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
