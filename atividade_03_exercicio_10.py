# Agenda Telefônica:
### Desenvolva um aplicativo de agenda telefônica que permita ao usuário adicionar, pesquisar, editar e excluir contatos.
### Bônus: armazene a agenda telefônica em um arquivo e carregue-a quando o aplicativo for iniciado.

import json

def carregar_agenda():
    try:
        with open("agenda.json", "r") as arquivo:
            agenda = json.load(arquivo)
    except FileNotFoundError:
        agenda = {}
    return agenda

def salvar_agenda(agenda):
    with open("agenda.json", "w") as arquivo:
        json.dump(agenda, arquivo, indent=4)

def adicionar_contato(agenda, nome, telefone):
    agenda[nome] = telefone
    salvar_agenda(agenda)
    print(f"Contato '{nome}' adicionado com sucesso!")

def pesquisar_contato(agenda, nome):
    if nome in agenda:
        print(f"Nome: {nome}, Telefone: {agenda[nome]}")
    else:
        print(f"Contato '{nome}' não encontrado na agenda.")

def editar_contato(agenda, nome, novo_telefone):
    if nome in agenda:
        agenda[nome] = novo_telefone
        salvar_agenda(agenda)
        print(f"Contato '{nome}' editado com sucesso!")
    else:
        print(f"Contato '{nome}' não encontrado na agenda.")

def excluir_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        salvar_agenda(agenda)
        print(f"Contato '{nome}' excluído com sucesso!")
    else:
        print(f"Contato '{nome}' não encontrado na agenda.")

def menu():
    print("Agenda como números telefonicos")
    agenda = carregar_agenda()

    while True:
        print("\nOpções:")
        print("1. Adicionar Contato")
        print("2. Pesquisar Contato")
        print("3. Editar Contato")
        print("4. Excluir Contato")
        print("5. Sair")

        escolha = input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            adicionar_contato(agenda, nome, telefone)
        elif escolha == "2":
            nome = input("Digite o nome do contato a ser pesquisado: ")
            pesquisar_contato(agenda, nome)
        elif escolha == "3":
            nome = input("Digite o nome do contato a ser editado: ")
            novo_telefone = input("Digite o novo telefone: ")
            editar_contato(agenda, nome, novo_telefone)
        elif escolha == "4":
            nome = input("Digite o nome do contato a ser excluído: ")
            excluir_contato(agenda, nome)
        elif escolha == "5":
            print("Saindo do aplicativo.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()
