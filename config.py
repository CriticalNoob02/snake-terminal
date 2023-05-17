def Board(lenth=5):
    board = []
    for i in range(lenth):
        board.append([])
        for e in range(lenth):
            board[i].append(['_'])
    
    board[0][0] = ['O']

    return board
#
def Worm():
    worm = [
        {'Coluna': 0, 'Linha':0},
        ]
    return worm
#