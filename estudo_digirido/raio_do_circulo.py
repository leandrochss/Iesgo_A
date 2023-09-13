# Exercício 5: Faça um programa em que o usuário digita o raio de um círculo em m e o programa retorna no console a área do círculo em m² e o perímetro em m.
import math

def calcula_circulo():
    raio = float(input("Digite o raio do círculo em metros: "))
    area = math.pi * (raio ** 2)
    perimetro = 2 * math.pi * raio
    print("A área do círculo é {:.2f} m² e o perímetro é {:.2f} m.".format(area, perimetro))

calcula_circulo()
