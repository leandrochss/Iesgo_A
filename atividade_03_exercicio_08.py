# Jogo de Adivinhação:
###Implemente um jogo simples em que o computador escolhe um número aleatório e o usuário tenta adivinhar o número.
### Bônus: faça o computador informar se o número inserido pelo usuário é maior ou menor que o número escolhido pelo computador.

import random

# Gerar um número aleatório de 1 a 100
numero_aleatorio = random.randint(1, 100)

# Contador de tentativas
tentativas = 0

print("Bem-Vindo ao jogo onde você adivinha o número!")
print("Tente adivinhar o número de 1 a 100.")

while True:
    tentativa = int(input("Digite um número:"))
    tentativas += 1

    if tentativa == numero_aleatorio:
        print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
        break
    elif tentativa < numero_aleatorio:
        print("Errou você foi neymar! Tente um número maior.")
    else:
        print("Errou você foi lula! Tente um número menor.")
