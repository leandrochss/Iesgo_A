# Atividade 8

def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador 

def substituir_python_por_java(texto):
    return texto.replace("Python", "Java")

def converter_para_minusculas(texto):
    return texto.lower()

def encontrar_palavras_unicas(texto):
    palavras = texto.lower().split()
    palavras_unicas = set(palavras)
    return palavras_unicas

def imprimir_palavras_ordem_alfabetica(texto):
    palavras = texto.lower().split()
    palavras.sort()
    for palavra in palavras:
        print(palavra)

def exibir_menu():
    print("Menu de Opções:")
    print("1 Conte o número total de palavras digitadas.")
    print("2 Conte o número de vogais na palavra digitada.")
    print("3 Substitua todas as ocorrências da palavra 'Python' por 'Java'.")
    print("4 Converta todas as letras da string para minúsculas.")
    print("5 Crie uma lista com todas as palavras únicas encontradas na string.")
    print("6 Imprima as palavras na string em ordem alfabética.")
    print("0. Sair")

texto = input("Digite um texto: ")

while True:
    exibir_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        total_palavras = contar_palavras(texto)
        print("Total de palavras:", total_palavras)
    elif opcao == '2':
        total_vogais = contar_vogais(texto)
        print("Total de vogais:", total_vogais)
    elif opcao == '3':
        texto = substituir_python_por_java(texto)
        print("Texto com sybstituição:", texto)
    elif opcao == '4':
        texto = converter_para_minusculas(texto)
        print("Texto em minúsculas:", texto)
    elif opcao == '5':
        palavras_unicas = encontrar_palavras_unicas(texto)
        print("Palavras únicas:", palavras_unicas)
    elif opcao == '6':
        imprimir_palavras_ordem_alfabetica(texto)
    elif opcao == '0':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Digite novamente.")