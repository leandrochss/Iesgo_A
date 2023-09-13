#Exercício 10: Faça um programa que solicita ao usuário escrever um texto e conta quantas vezes a letra "a" aparece no texto.
def conta_letras():
    texto = input("Escreva um texto: ")
    contador = texto.lower().count('a')
    print("A letra 'a' aparece", contador, "vezes no texto.")

conta_letras()
