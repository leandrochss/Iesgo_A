# Exercício 18 -  Gere um número aleatório entre 1 e 9 (incluindo 1 e 9). 
# Peça ao usuário para adivinhar o número e, em seguida, diga a eles se eles adivinharam, se o número é menor que o seu palpite ou se número é maior que o seu palpite.

# Extras:

# 1. Continue o jogo até que o usuário digite "sair".
# 2. Acompanhe quantas tentativas o usuário fez e, quando o jogo terminar, imprima este número.

import random

# Inicializa o contador de tentativas
tentativas = 0

while True:
    # Gera um número aleatório entre 1 e 9
    numero = random.randint(1, 9)

    # Solicita ao usuário para adivinhar o número
    palpite = input("Adivinhe o número entre 1 e 9 ou digite 'sair' para terminar o jogo: ")

    # Verifica se o usuário quer sair do jogo
    if palpite.lower() == 'sair':
        break

    # Converte o palpite para um número inteiro
    palpite = int(palpite)

    # Incrementa o contador de tentativas
    tentativas += 1

    # Verifica se o usuário adivinhou o número
    if palpite == numero:
        print("Parabéns! Você adivinhou o número.")
    elif palpite < numero:
        print("O número é maior que o seu palpite.")
    else:
        print("O número é menor que o seu palpite.")

# Imprime o número de tentativas quando o jogo termina
print(f"Você fez {tentativas} tentativas.")
