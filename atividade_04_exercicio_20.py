# Exercício 20 - Crie um programa que solicita ao usuário inserir uma string longa contendo várias palavras. Em seguida, o programa deve imprimir:
# 1. uma string contendo apenas as palavras que começam com uma letra maiúscula.
# 2. uma string contendo apenas as palavras que terminam com uma vogal.
# 3. uma string contendo apenas as palavras que têm mais de 5 letras.
# 4. uma string contendo o inverso de cada palavra na string original. (Nota: não use a função reverse() do Python, faça isso manualmente!)
# Solicita ao usuário inserir uma string longa contendo várias palavras

texto = input("Digite uma string longa contendo várias palavras: ")

# Divide a string em palavras
palavras = texto.split()

# Cria listas para armazenar as palavras que satisfazem cada condição
palavras_maiuscula = [palavra for palavra in palavras if palavra[0].isupper()]
palavras_vogal = [palavra for palavra in palavras if palavra[-1] in 'aeiouAEIOU']
palavras_longas = [palavra for palavra in palavras if len(palavra) > 5]
palavras_inverso = [''.join(reversed(palavra)) for palavra in palavras]

# Imprime as strings
print("Palavras que começam com uma letra maiúscula: " + ' '.join(palavras_maiuscula))
print("Palavras que terminam com uma vogal: " + ' '.join(palavras_vogal))
print("Palavras que têm mais de 5 letras: " + ' '.join(palavras_longas))
print("Inverso de cada palavra na string original: " + ' '.join(palavras_inverso))
