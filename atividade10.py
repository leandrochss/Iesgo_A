# Atividade 10

def criar_arte_ascii(caractere, altura):
    for i in range(1, altura + 1):
        linha = caractere * i 
        print(linha)

caractere = input("Digite um caractere para o padrão de arte: ")
altura = int(input("Digite a altura do padrão de arte (número inteiro ):"))

criar_arte_ascii(caractere, altura)
