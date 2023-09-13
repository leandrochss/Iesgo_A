# Exercício 10 - Escreva um programa que solicita ao usuário inserir um número inteiro positivo n e o programa retorna um dicionário que contém (i, i*i) para cada número inteiro positivo i menor ou igual a n.
# Use o dicionário para imprimir o quadrado de cada número inteiro positivo menor ou igual a n.
# Solicita ao usuário inserir um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Cria um dicionário que contém (i, i*i) para cada número inteiro positivo i menor ou igual a n
dicionario = {i: i*i for i in range(1, n + 1)}

# Imprime o quadrado de cada número inteiro positivo menor ou igual a n
for i in dicionario:
    print(f"O quadrado de {i} é {dicionario[i]}")
