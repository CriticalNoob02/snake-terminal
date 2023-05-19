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
            board[c][l] = [f'O']
        else:
            board[c][l] = ['o']
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
        board[c][l] = ['_']

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
    board[c][l] = ['f']

    return board
#
def Console(board, worm, food):
    """Rederniza o tabuleiro no terminal
        --
        Função responsável por redernizar o tabuleiro dentro do terminal.

        retorna: `nada`
    """
    os.system('clear')
    board = saveFood(board, food)
    board = saveBoard(board, worm)

    for i in range(len(board)):
        print((board[i]))
        # line = []
        # for e in range(len(board[i])):
        #     if board[i][e] == '_':
        #         newStyle, base = ColorsTerminal(0,0,0)
        #         line.append(f'{newStyle}_{base}')
        #     elif board[i][e] == 'f':
        #         newStyle, base = ColorsTerminal(0,2,0)
        #         line.append(f'{newStyle}F{base}')
        #     elif board[i][e] == 'O':
        #         newStyle, base = ColorsTerminal(0,3,0)
        #         line.append(f'{newStyle}_{base}')
        #     elif board[i][e] == 'o':
        #         newStyle, base = ColorsTerminal(0,7,0)
        #         line.append(f'{newStyle}_{base}')
        #     else:
        #         newStyle, base = ColorsTerminal(0,7,0)
        #         line.append(f'{newStyle}_{base}')
        # print(map(str ,line))

    board = clearBoard(board, worm)
    time.sleep(1)
#