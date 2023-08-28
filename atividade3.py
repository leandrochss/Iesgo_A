# Atividade 3: Crie uma aplicação que solicite ao usuário digite seu nome completo e imprima no console, mas às vezes aparece a letra "a",

def contagem_letra_a(nome):
    contador = 0
    for letra in nome:
        if letra.lower() =='a':
            contador += 1
    return contador
nome_completo = input("Digite seu nome completo:")
quantidade_a = contagem_letra_a(nome_completo)
print("O nome digitado possui", quantidade_a, "Letra(s) 'a'.")