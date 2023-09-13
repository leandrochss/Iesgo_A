# Exercício 7: Faça um programa que solicita ao usuário inserir um número inteiro e retorna se ele é primo.
def verifica_primo():
    numero = int(input("Digite um número inteiro: "))
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                print(numero, "não é um número primo.")
                break
        else:
            print(numero, "é um número primo.")
    else:
        print(numero, "não é um número primo.")

verifica_primo()
