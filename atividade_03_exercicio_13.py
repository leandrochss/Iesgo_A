# Par ou ímpar:
### Crie um jogo simples em que o computador escolhe um número aleatório e o usuário tenta adivinhar se o número é par ou ímpar.
### Bônus: permita que o usuário jogue contra outro usuário humano.

import random

def par_ou_impar():
    numero = random.randint(1, 100)
    escolha1 = input("Player 1, o número é par ou ímpar? (P/I): ")
    escolha2 = input("Player 2, o número é par ou ímpar? (P/I): ")
    if (numero % 2 == 0 and escolha1.upper() == "P") or (numero % 2 != 0 and escolha1.upper() == "I"):
        print("Player 1 acertou! O número era", numero)
    else:
        print("Player 1 errou. O número era", numero)
    if (numero % 2 == 0 and escolha2.upper() == "P") or (numero % 2 != 0 and escolha2.upper() == "I"):
        print("Player 2 acertou! O número era", numero)
    else:
        print( "Player 2 errou. O número era", numero)

par_ou_impar()
