##Exercício 1.1: Sistema de Biblioteca

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = "disponível"

class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.membros = {}

    def adicionar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def registrar_membro(self, membro):
        self.membros[membro.nome] = membro

    def emprestar_livro(self, titulo_livro, nome_membro):
        if titulo_livro in self.livros and self.livros[titulo_livro].status == "disponível":
            self.livros[titulo_livro].status = "emprestado"
            self.membros[nome_membro].livros_emprestados.append(titulo_livro)

    def retornar_livro(self, titulo_livro, nome_membro):
        if titulo_livro in self.membros[nome_membro].livros_emprestados:
            self.membros[nome_membro].livros_emprestados.remove(titulo_livro)
            self.livros[titulo_livro].status = "disponível"

    # Desafio
    def remover_livro(self, titulo_livro):
        if titulo_livro in self.livros:
            del self.livros[titulo_livro]

    def remover_membro(self, nome_membro):
        if nome_membro in self.membros:
            del self.membros[nome_membro]

    def buscar_por_nome(self, nome):
        if nome in self.livros:
            return f"Livro: {self.livros[nome].titulo}, Autor: {self.livros[nome].autor}, Status: {self.livros[nome].status}"
        elif nome in self.membros:
            return f"Membro: {self.membros[nome].nome}, Livros emprestados: {', '.join(self.membros[nome].livros_emprestados)}"
        else:
            return "Não encontrado"


def main():
    biblioteca = Biblioteca()

    while True:
        print("\nOpções:")
        print("1. Adicionar Livro")
        print("2. Registrar Membro")
        print("3. Emprestar Livro")
        print("4. Retornar Livro")
        print("5. Remover Livro")
        print("6. Remover Membro")
        print("7. Buscar por Nome")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            livro = Livro(titulo, autor)
            biblioteca.adicionar_livro(livro)
            print("Livro adicionado com sucesso!")

        elif opcao == "2":
            nome = input("Digite o nome do membro: ")
            membro = Membro(nome)
            biblioteca.registrar_membro(membro)
            print("Membro registrado com sucesso!")

        elif opcao == "3":
            titulo_livro = input("Digite o título do livro a ser emprestado: ")
            nome_membro = input("Digite o nome do membro: ")
            biblioteca.emprestar_livro(titulo_livro, nome_membro)

        elif opcao == "4":
            titulo_livro = input("Digite o título do livro a ser retornado: ")
            nome_membro = input("Digite o nome do membro: ")
            biblioteca.retornar_livro(titulo_livro, nome_membro)

        elif opcao == "5":
            titulo_livro = input("Digite o título do livro a ser removido: ")
            biblioteca.remover_livro(titulo_livro)

        elif opcao == "6":
            nome_membro = input("Digite o nome do membro a ser removido: ")
            biblioteca.remover_membro(nome_membro)

        elif opcao == "7":
            nome = input("Digite o nome do livro ou membro a ser buscado: ")
            resultado = biblioteca.buscar_por_nome(nome)
            print(resultado)

        elif opcao == "8":
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
