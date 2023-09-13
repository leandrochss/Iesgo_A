# Exercício 13 - Crie um programa que entrega a raiz quadrada de um número inteiro positivo n com uma precisão de 0.001.

def raiz_quadrada(n, precisao=0.001):
    # Inicializa a estimativa da raiz quadrada como n
    raiz = n

    while abs(raiz * raiz - n) > precisao:
        raiz = (raiz + n / raiz) / 2

    return raiz

# Solicita ao usuário inserir um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Calcula e imprime a raiz quadrada do número
print(f"A raiz quadrada de {n} é aproximadamente {raiz_quadrada(n)}")
