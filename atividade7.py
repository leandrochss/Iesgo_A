# Atividade 7  

nome_sobrenome = input("Digite seu nome e sobrenome: ")

# Separando o nome e sobrenome usando o espaço como separador
nome_sobrenome_lista = nome_sobrenome.split()

if len(nome_sobrenome_lista) == 2:
    nome_usuario, sobrenome_usuario = nome_sobrenome_lista

    # Transformando o nome em letras secretas (maiúsculas)
    nome_secreto = nome_usuario.upper()

    # Transformando o sobrenome em letras minúsculas e removendo espaços
    sobrenome_secreto = sobrenome_usuario.lower().replace(" ", "")

    # Criando o nome completo
    nome_completo = nome_secreto + " " + sobrenome_secreto

    # Imprimindo o nome completo em letras minúsculas
    print("Nome completo em letras minúsculas:", nome_completo)

    # Calculando e imprimindo o tamanho do nome completo
    tamanho_nome_completo = len(nome_completo)
    print("Tamanho do nome completo:", tamanho_nome_completo)
else:
    print("Você precisa digitar o nome e sobrenome separados por um espaço.")
