# Exercício 6 - Escreva um aplicativo que solicita ao usuário inserir um número e retorna o seu fatorial.
# Função para calcular o fatorial de um número
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

# Solicita ao usuário inserir um número
num = int(input("Digite um número: "))

# Calcula e imprime o fatorial do número
print(f"O fatorial de {num} é {fatorial(num)}")
