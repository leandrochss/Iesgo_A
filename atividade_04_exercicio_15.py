# Exercício 15 - Crie um programa em que o usuário deve responder no terminal quantos números de Fibonacci ele deseja ver. 
#Em seguida, o programa deve imprimir os números de Fibonacci na tela em uma lista separada por vírgulas.
# Função para gerar a sequência de Fibonacci
def fibonacci(n):
    # Inicializa a sequência de Fibonacci
    fib = [0, 1]

    # Gera os números de Fibonacci
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

    return fib[:n]

# Solicita ao usuário quantos números de Fibonacci ele deseja ver
n = int(input("Quantos números de Fibonacci você deseja ver? "))

# Gera e imprime os números de Fibonacci
print(', '.join(map(str, fibonacci(n))))
