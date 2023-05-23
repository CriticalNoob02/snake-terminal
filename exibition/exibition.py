import os
import time
from exibition.colors import ColorsTerminal

def saveBoard(board, worm):
    """Adiciona minhoca no tabuleiro
        --
        Função responsável por redernizar a cabeça e corpo da minhoca no tabuleiro.

        retorna: `board`
    """
    for i in range(len(worm)):
        l = worm[i]['Linha']
        c = worm[i]['Coluna']
        if i == 0:
            newStyle, base = ColorsTerminal(0,3,0)
            board[c][l] = f'|{newStyle} O {base}|'
        else:
            newStyle, base = ColorsTerminal(0,1,0)
            board[c][l] = f'|{newStyle} o {base}|'
    return board
#
def clearBoard(board, worm):
    """Limpa o tabuleiro
        --
        Função responsável por limpar o tabuleiro.

        retorna: `board`
    """
    for i in range(len(worm)):
        l = worm[i]['Linha']
        c = worm[i]['Coluna']
        newStyle, base = ColorsTerminal(0, 3, 0)
        board[c][l] = f'|{newStyle} _ {base}|'

    return board
#
def saveFood(board, food):
    """Adiciona alimento no tabuleiro
        --
        Função responsável por redernizar o alimento no tabuleiro.

        retorna: `board`
    """
    # TODO: chamar essa função antes da função saveBoard
    l = food['Linha']
    c = food['Coluna']
    newStyle, base = ColorsTerminal(0, 2, 0)
    board[c][l] = f'|{newStyle} d {base}|'

    return board
#
def Console(board, worm, food, end=True):
    """Rederniza o tabuleiro no terminal
        --
        Função responsável por redernizar o tabuleiro dentro do terminal.

        retorna: `nada`
    """
    if not end:
        print('Game Over - Perdeu playboy')
    else: 
        os.system('clear')
        board = saveFood(board, food)
        board = saveBoard(board, worm)

        for line in board:
            for element in line:
                print(element, end='',)
            print()

        board = clearBoard(board, worm)
#