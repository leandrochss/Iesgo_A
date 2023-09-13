# Exercício 6: Faça um programa que solicita o ano de nascimento do usuário e retorna o seu signo no horóscopo chinês.

def horoscopo_chines():
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    signos = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Cabra']
    signo = signos[ano_nascimento % 12]
    print("O seu signo no horóscopo chinês é: ", signo)

horoscopo_chines()
