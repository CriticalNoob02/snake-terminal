import os
import time

def saveBoard(board, worm):
    for i in range(len(worm)):
        l = worm[i]['Linha']
        c = worm[i]['Coluna']
        if i == 0:
            board[c][l] = ['O']
        else:
            board[c][l] = ['o']
    return board
#
def clearBoard(board, worm):
    for i in range(len(worm)):
        l = worm[i]['Linha']
        c = worm[i]['Coluna']
        board[c][l] = ['_']

    return board
#
def saveFood(board, food):
    # TODO: chamar essa função antes da função saveBoard
    l = food['Linha']
    c = food['Coluna']
    board[c][l] = ['f']

    return board
#
def Console(board, worm, food):
    os.system('clear')
    board = saveFood(board, food)
    board = saveBoard(board, worm)

    for i in range(len(board)):
        print(board[i])

    board = clearBoard(board, worm)
    time.sleep(1)
#