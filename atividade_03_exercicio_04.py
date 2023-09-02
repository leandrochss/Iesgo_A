# Contador de Palavras:
### Faça um programa que conte quantas palavras há em uma frase inserida pelo usuário.
### Bônus: faça o programa retornar a frase com todas as letras maiúsculas e sem espaços em branco.

# Socilitar uma frase ao usuário
frase = input("Digite sua frase: ")

# Dividir a frase em palavras
palavras = frase.split()

# Contador o número de palavras na frase
num_palavras = len(palavras)

# Remover espaços em branco e transformar a frase em letras maiúsculas 
frase_maiusculas_sem_espacos = frase.upper().replace(" ", "")

# Exibir o número de palavras e a frase em letras maiúsculas sem espaços 
print(f"Número de palavras na frase: {num_palavras}")
print(f"Frase em letras maiúsculas sem espaços: {frase_maiusculas_sem_espacos}")
