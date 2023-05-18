import random
#
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
def GenerationFood(board, worm):
    validationC = False
    validationL = False
    c = random.choice(range(0,len(board)))
    l = random.choice(range(0,len(board)))
    while not validationC and not validationL:      
        for i in range(len(worm)):

            if c == worm[i]['Coluna']:
                print(f"coluna gerada: {c}, coluna minhoca:{worm[i]['Coluna']}")
                c = random.choice(range(0,len(board)))
            else:
                validationC = True

            if l == worm[i]['Linha']:
                print(f"coluna gerada: {l}, coluna minhoca:{worm[i]['Linha']}")
                l = random.choice(range(0,len(board)))
            else:
                validationL = True
    food = {'Coluna': c, 'Linha': l}
    return food