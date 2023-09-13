# Exercício 19 - Crie um jogo da velha para ser jogado por dois jogadores no terminal.
# Esse jogo deve ser capaz de imprimir o tabuleiro, solicitar ao jogador 1 que insira a sua jogada, solicitar ao jogador 2 que insira a sua jogada e verificar se o jogo terminou e quem ganhou.

def print_tabuleiro(tab):
    print(' ' + tab[7] + ' | ' + tab[8] + ' | ' + tab[9])
    print('---|---|---')
    print(' ' + tab[4] + ' | ' + tab[5] + ' | ' + tab[6])
    print('---|---|---')
    print(' ' + tab[1] + ' | ' + tab[2] + ' | ' + tab[3])

def verifica_vencedor(tab, jogada):
    vencedor = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    for v in vencedor:
        if tab[v[0]] == tab[v[1]] == tab[v[2]] == jogada:
            return True
    return False

def jogo():
    tab = [' '] * 10
    jogada = 'X'
    while True:
        print_tabuleiro(tab)
        pos = int(input(f'Jogador {jogada}, escolha uma posição: '))
        if tab[pos] == ' ':
            tab[pos] = jogada
            if verifica_vencedor(tab, jogada):
                print_tabuleiro(tab)
                print(f'Jogador {jogada} ganhou!')
                break
            if jogada == 'X':
                jogada = 'O'
            else:
                jogada = 'X'
        else:
            print('Posição inválida. Tente novamente.')

jogo()
