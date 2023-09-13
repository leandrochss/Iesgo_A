# Exercício 12 - Escreva um programa que contenha uma função com o seu nome que solicita ao usuário inserir um texto e retorna o número de letras que o texto contém que também compõem o seu nome.
def bing():
    # Solicita ao usuário inserir um texto
    texto = input("Digite um texto: ")

    # Converte o texto para minúsculas para facilitar a comparação
    texto = texto.lower()

    # Define as letras que compõem o meu nome
    letras_do_nome = 'bing'

    # Conta o número de letras no texto que também estão no meu nome
    contador = sum(texto.count(letra) for letra in letras_do_nome)

    # Retorna o número de letras
    return contador

# Chama a função e imprime o resultado
print(f"O número de letras no texto que também compõem o meu nome é {bing()}")
