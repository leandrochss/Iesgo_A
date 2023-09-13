# Exercício 8 - Escreva um programa que solicita ao usuário inserir um número inteiro positivo n e o programa retorna a soma de todos os números inteiros positivos entre 1 e n que são divisíveis por 3 ou 5.
# Solicita ao usuário inserir um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Calcula a soma de todos os números inteiros positivos entre 1 e n que são divisíveis por 3 ou 5
soma = sum(i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0)

# Imprime a soma
print(f"A soma de todos os números inteiros positivos entre 1 e {n} que são divisíveis por 3 ou 5 é {soma}")
