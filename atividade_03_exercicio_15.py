# Gerador de Sim ou Não:
### Crie um programa que permita ao usuário inserir uma pergunta e, em seguida, exiba uma resposta aleatória de sim ou não.
### Bônus: adicione a opção talvez ao gerador de respostas.

import random

def sim_nao_talvez():
    pergunta = input("Insira sua pergunta: ")
    resposta = random.choice(["Sim", "Não", "Talvez"])
    print("Resposta:", resposta)

sim_nao_talvez()
