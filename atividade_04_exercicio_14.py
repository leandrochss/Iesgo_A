# Exercício 14 - Crie um programa que solicita ao usuário inserir um número inteiro positivo n e o programa retorna se o número é par ou ímpar.
# Solicita ao usuário inserir um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é par ou ímpar
if n % 2 == 0:
    print(f"O número {n} é par.")
else:
    print(f"O número {n} é ímpar.")
