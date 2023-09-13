# Exercício 11 - Escreva um programa em que o usuário insere o valor do raio de uma esfera em m e o programa retorna o volume da esfera em litros.

import math

# Solicita ao usuário inserir o valor do raio da esfera em metros
raio = float(input("Digite o valor do raio da esfera em metros: "))

# Calcula o volume da esfera em metros cúbicos
volume_m3 = (4/3) * math.pi * (raio**3)

# Converte o volume para litros (1 m^3 = 1000 litros)
volume_litros = volume_m3 * 1000

# Imprime o volume da esfera em litros
print(f"O volume da esfera é {volume_litros} litros")
