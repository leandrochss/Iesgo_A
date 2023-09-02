#Analisador de String:
### Faça um programa que analise uma string inserida pelo usuário e conte quantas letras maiúsculas, minúsculas, dígitos e caracteres especiais ela contém.
### Bônus: faça o programa retornar quantas palavras há na string.

def analisar_string(string):
    # Inicialize contadores
    maiusculas = 0
    minusculas = 0
    digitos = 0
    especiais = 0
    palavras = len(string.split())

    # Itere através dos caracteres na string
    for char in string:
        if char.isupper():
            maiusculas += 1
        elif char.islower():
            minusculas += 1
        elif char.isdigit():
            digitos += 1 
        else:
            especiais += 1 
            
    return maiusculas, minusculas, digitos, especiais, palavras

# Socilitar uma string ao usuário
string = input("Digite uma string: ")

# Chamar a função paa anlisar a string
maiusculas, minusculas, digitos, especiais, palavras = analisar_string(string)

# Exebir os resultados
print(f"Número de letras maiúscualas: {maiusculas}")
print(f"Número de letras minúsculas: {minusculas}")
print(f"Número de dígitos: {digitos}")
print(f"Número de caracteres especiais: {especiais}")
print(f"Número de palavras no string: {palavras}")
