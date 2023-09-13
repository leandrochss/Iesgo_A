# Exerício 2 - Escreva um programa que solicita dois números inteirtos (sendo o primeiro o limite inferior e o segundo o limite superior) e exibe todos os números pares entre esses limites.
# Solicita o limite inferior
limite_inferior = int(input("Digite o limite inferior: "))

# Solicita o limite superior
limite_superior = int(input("Digite o limite superior: "))

# Percorre todos os números entre os limites
for i in range(limite_inferior, limite_superior + 1):
    # Verifica se o número é par
    if i % 2 == 0:
        print(i)
