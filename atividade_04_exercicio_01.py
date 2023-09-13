# Exercício 1 -  Escreva um programa que deve listar no console todos os números divisíveis por 5 entre 1 e 100 (inclusive).

for i in range(1, 101):
    if i % 5 == 0:
        print(i)
