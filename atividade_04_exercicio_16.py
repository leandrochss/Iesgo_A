#Exercício 16 - Considere a seguinte lista: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] ----> e escreva um programa que imprime todos os elementos da lista que são menores que 5.
# Define a lista
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Solicita ao usuário um número
num = int(input("Digite um número: "))

# Cria uma nova lista que contém todos os elementos menores que o número fornecido pelo usuário
nova_lista = [i for i in a if i < num]

# Imprime a nova lista
print(nova_lista)
