# Exercício 9: Usando o método random(), crie um programa que solicita ao usuário que adivinhe um número inteiro entre 1 e 10.
# Se o usuário digitar um número menor que 1 ou maior que 10, solicite que ele insira um número válido. 
#Se o usuário digitar um número válido, verifique se o número que o usuário digitou é igual ao número gerado aleatoriamente pelo programa. 
#Se o número for igual, imprima "Você acertou!". Caso contrário, imprima "Você errou!".

import random

def adivinhe_o_numero():
    numero_aleatorio = random.randint(1, 10)
    while True:
        numero_usuario = int(input("Adivinhe um número inteiro entre 1 e 10: "))
        if numero_usuario < 1 or numero_usuario > 10:
            print("Por favor, insira um número válido.")
        else:
            if numero_usuario == numero_aleatorio:
                print("Você acertou!")
                break
            else:
                print("Você errou!")

adivinhe_o_numero()
