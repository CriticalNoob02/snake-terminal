import os
import time

def saveBoard(board, worm):
    for i in range(len(worm)):
        l = worm[i]['Linha']
        c = worm[i]['Coluna']
        board[c][l] = ['O']

    return board
#
def clearBoard(board, worm):
    for i in range(len(worm)):
        l = worm[i]['Linha']
        c = worm[i]['Coluna']
        board[c][l] = ['_']

    return board

def Console(board, worm):
    os.system('clear')
    board = saveBoard(board, worm)

    for i in range(len(board)):
        print(board[i])

    board = clearBoard(board, worm)
    time.sleep(1)
