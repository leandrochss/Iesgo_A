# Exercício 9 - Escreva um programa que solicita ao usuário as dimensões de um retângulo e o programa retorna o perímetro e a área do retângulo.
# Solicita ao usuário a largura e a altura do retângulo
largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

# Calcula o perímetro e a área do retângulo
perimetro = 2 * (largura + altura)
area = largura * altura

# Imprime o perímetro e a área
print(f"O perímetro do retângulo é {perimetro}")
print(f"A área do retângulo é {area}")
