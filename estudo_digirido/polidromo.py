# Exercício 3: Crie um programa em que o usuário insira uma palavra e o programa retorna se a palavra é palíndromo ou não.

def verifica_palindromo():
    palavra = input("Insira uma palavra: ")
    palavra = palavra.lower()
    if palavra == palavra[::-1]:
        print("A palavra é um palíndromo.")
    else:
        print("A palavra não é um palíndromo.")

verifica_palindromo()
