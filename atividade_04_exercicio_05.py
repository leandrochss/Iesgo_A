# Exercício 5 - Escreva um programa que encontra quais números são divisíveis por 7 e não são múltiplos de 5, entre 2000 e 3200 (inclusive).
# Imprima o seu resultado no console em uma única linha separada por vírgulas.

numeros = []

# Percorre todos os números entre 2000 e 3200 (inclusive)
for i in range(2000, 3201):
    # Verifica se o número é divisível por 7 e não é múltiplo de 5
    if i % 7 == 0 and i % 5 != 0:
        numeros.append(str(i))

# Imprime os números em uma única linha separada por vírgulas
print(','.join(numeros))
