# Pedra, Papel e Tesoura:
### Crie um jogo simples de pedra, papel e tesoura em que o computador escolhe aleatoriamente uma das três opções e o usuário tenta vencer o computador escolhendo sua própria opção.
### Bônus: dê ao usuário a opção de jogar com outro jogador humano.

import random

def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    
    # Solicita ao jogador que escolha entre "computador" e "jogador"
    adversario = input("Você quer jogar contra o computador ou outro jogador? Digite 'computador' ou 'jogador': ").lower()
    
    # Verifica se a escolha do adversário é válida
    while adversario not in ["computador", "jogador"]:
        adversario = input("Escolha inválida. Digite 'computador' ou 'jogador': ").lower()
    
    if adversario == "computador":
        # Joga contra o computador
        jogador = input("Jogador, escolha pedra, papel ou tesoura: ").lower()
        
        # Verifica se a escolha do jogador é válida
        while jogador not in opcoes:
            jogador = input("Escolha inválida. Jogador, escolha pedra, papel ou tesoura: ").lower()
        
        # Escolha aleatória do computador
        computador = random.choice(opcoes)
        
        # Determina o vencedor com base nas escolhas
        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "papel" and computador == "pedra") or \
             (jogador == "tesoura" and computador == "papel"):
            print("Jogador venceu! O computador escolheu", computador)
        else:
            print("Computador venceu! O computador escolheu", computador)
    
    else:
        # Joga contra outro jogador humano
        jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()
        
        # Verifica se a escolha do jogador 1 é válida
        while jogador1 not in opcoes:
            jogador1 = input("Escolha inválida. Jogador 1, escolha pedra, papel ou tesoura: ").lower()
        
        jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").lower()
        
        # Verifica se a escolha do jogador 2 é válida
        while jogador2 not in opcoes:
            jogador2 = input("Escolha inválida. Jogador 2, escolha pedra, papel ou tesoura: ").lower()
        
        # Determina o vencedor com base nas escolhas dos jogadores
        if jogador1 == jogador2:
            print("Empate!")
        elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
             (jogador1 == "papel" and jogador2 == "pedra") or \
             (jogador1 == "tesoura" and jogador2 == "papel"):
            print("Jogador 1 venceu! Jogador 2 escolheu", jogador2)
        else:
            print("Jogador 2 venceu! Jogador 1 escolheu", jogador1)

# Chama a função para iniciar o jogo
pedra_papel_tesoura()
