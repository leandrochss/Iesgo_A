# Exercício 7 - Escreva um programa em que o usuário insere um número inteiro positivo n e o programa retorna a soma de todos os números inteiros positivos entre 1 e n.
# Solicita ao usuário inserir um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Calcula a soma de todos os números inteiros positivos entre 1 e n
soma = sum(range(1, n + 1))

# Imprime a soma
print(f"A soma de todos os números inteiros positivos entre 1 e {n} é {soma}")

