# Calculadora de Fatorial:
### Crie uma calculadora que permita ao usuário calcular o fatorial de qualquer número.
### Bônus: faça o programa retornar um erro se o usuário inserir um número negativo.

def fatorial(n):
    if n < 0:
        raise ValueError("Não foi possível calcular o fatorial de um número negativo")
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

try:
    numero = int(input("Insira um número para calcular o fatorial: "))
    resultado = fatorial(numero)
    print("O fatorial de", numero, "é", resultado)
except ValueError as e:
    print(e)
