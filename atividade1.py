def substituir_vogais(palavra):
    vogais = "aeiouAEIOU"
    palavra_substituida = ""

    for letra in palavra:
        if letra in vogais:
            palavra_substituida += "*"
        else:
            palavra_substituida += letra
    return palavra_substituida

palavra_usuario = input("Digite uma palavra: ")
palavra_substituida = substituir_vogais(palavra_usuario)
print("Palavra substituída:", palavra_substituida)