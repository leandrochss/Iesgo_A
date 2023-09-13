# Exercicio 4: Faça um programa que solicita ao usuário escrever o nome das frutas que ele deseja comprar. O usuário deve digitar as frutas até digitar a palavra "sair". 
#O programa deve imprimir na tela a lista de frutas que o usuário deseja comprar.
def lista_de_compras():
    frutas = []
    while True:
        fruta = input("Digite o nome da fruta que deseja comprar ou 'sair' para finalizar: ")
        if fruta.lower() == 'sair':
            break
        frutas.append(fruta)
    print("A lista de frutas que você deseja comprar é: ", frutas)

lista_de_compras()
