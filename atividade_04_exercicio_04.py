# Exercício 4 - Escreva um programa que solicita um número inteiro e exibe todos os seus divisores primos.
# Função para verificar se um número é primo
def eh_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# Solicita um número inteiro
num = int(input("Digite um número inteiro: "))

print(f"Os divisores primos de {num} são:")

# Percorre todos os números até o número dado
for i in range(2, num + 1):
    # Verifica se o número é divisor e se é primo
    if num % i == 0 and eh_primo(i):
        print(i)
