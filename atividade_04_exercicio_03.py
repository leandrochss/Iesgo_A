# Exercício 3 - Escreva um programa que solicita um número inteiro e exibe todos os seus divisores.
# Solicita um número inteiro
num = int(input("Digite um número inteiro: "))

print(f"Os divisores de {num} são:")

# Percorre todos os números até o número dado
for i in range(1, num + 1):
    # Verifica se o número é divisor
    if num % i == 0:
        print(i)
