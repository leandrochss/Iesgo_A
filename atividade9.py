# Atividade 9 

def remover_vogais(texto):
    vogais = "aeiouAEIOU"
    texto_sem_vogais = ''.join(letra for letra in texto if letra not in vogais  )
    return texto_sem_vogais

texto = input("Digite um texto: ")
texto_sem_vogais = remover_vogais(texto)
print("Texto sem vogais:", texto_sem_vogais)