# Atividade 6: Crie uma aplicação que solicite ao usuário digite o seu nome e sobrenomes e imprima no console o nome com todas as letras secretas e o sobrenome com todas as letras minúsculas sem espaços entre o nome e os sobrenomes e sem alterar a variável original.
nome = input("Digite seu nome: ")
sobrenome = input( "Digite seu sobrenome: ")

nome_secreto = nome.upper()
sobrenome_minusculo = sobrenome.replace(" ", "").lower()

print("Nome secreto:", nome_secreto)
print("Sobrenome em minúsculo:", sobrenome_minusculo)