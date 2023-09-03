# Jogo da Velha:
### Crie um jogo da velha para dois jogadores que permite aos usuários inserir o local onde desejam inserir seu símbolo (X ou O) e mantenha uma contagem das vitórias de cada jogador.
### Bônus: permita que o usuário jogue contra o computador.

import random

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if all([c == jogador for c in tabuleiro[i]]) or all([c == jogador for c in [tabuleiro[j][i] for j in range(3)]]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True
    return False

def jogar_computador(tabuleiro, jogador):
    print("Vez do computador (", jogador, ")")
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            break

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador1 = "X"
    jogador2 = "O"
    jogadores = [jogador1, jogador2]
    vitorias = {jogador1: 0, jogador2: 0}
    jogar_computador_opcao = input("Deseja jogar contra o computador? (s/n): ").lower() == "s"

    while True:
        for jogador in jogadores:
            imprimir_tabuleiro(tabuleiro)
            if jogador == jogador1 or (jogador == jogador2 and not jogar_computador_opcao):
                print("Vez do jogador", jogador)
                while True:
                    try:
                        linha = int(input("Digite a linha (0, 1, 2): "))
                        coluna = int(input("Digite a coluna (0, 1, 2): "))
                        if tabuleiro[linha][coluna] == " ":
                            tabuleiro[linha][coluna] = jogador
                            break
                        else:
                            print("Essa posição já está ocupada. Tente novamente.")
                    except (ValueError, IndexError):
                        print("Entrada inválida. Tente novamente.")
            else:
                jogar_computador(tabuleiro, jogador)

            if verificar_vitoria(tabuleiro, jogador):
                imprimir_tabuleiro(tabuleiro)
                if jogador == jogador1 or not jogar_computador_opcao:
                    print("Jogador", jogador, "venceu!")
                else:
                    print("Computador venceu!")
                vitorias[jogador] += 1
                break

            if " " not in [c for linha in tabuleiro for c in linha]:
                imprimir_tabuleiro(tabuleiro)
                print("Empate!")
                break

        resposta = input("Deseja jogar novamente? (s/n): ").lower()
        if resposta != "s":
            break

    imprimir_tabuleiro(tabuleiro)
    print("Placar:")
    for jogador, vitoria in vitorias.items():
        print(jogador + ":", vitoria, "vitórias")

if __name__ == "__main__":
    jogo_da_velha()
