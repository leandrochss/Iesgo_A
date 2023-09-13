# Exercício 17 - Escreva um programa que solicita ao usuário inserir uma palavra e retorna se a palavra é um palíndromo ou não.
# Solicita ao usuário inserir uma palavra
palavra = input("Digite uma palavra: ")

# Verifica se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print(f"A palavra {palavra} é um palíndromo.")
else:
    print(f"A palavra {palavra} não é um palíndromo.")
