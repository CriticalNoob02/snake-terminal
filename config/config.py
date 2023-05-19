import random
#
def Board(lenth=5):
    """Gerar tabuleiro
        --
        Função responsável por gerar o campo que sera jogado.

        retorna: `board`
    """
    board = []
    for i in range(lenth):
        board.append([])
        for e in range(lenth):
            board[i].append(['_'])
    
    board[0][0] = ['O']

    return board
#
def Worm():
    """Gerar minhoca
        --
        Função responsável por gerar as coordenadas iniciais da minhoca.
    
        retorna: `worm`
    """
    worm = [
        {'Coluna': 0, 'Linha':0},
        ]
    return worm
#
def GenerationFood(board, worm):
    """Gerar alimentos
        --
        Função responsável por gerar uma nova coordenada para a próxima comida.

        Verifica se a coordenada gerada está dentro das coordenadas da minhoca. 
    
        retorna: `food`
    """
    validationC = False
    validationL = False
    c = random.choice(range(0,len(board)))
    l = random.choice(range(0,len(board)))
    while not validationC and not validationL:      
        for i in range(len(worm)):

            if c == worm[i]['Coluna']:
                c = random.choice(range(0,len(board)))
            else:
                validationC = True

            if l == worm[i]['Linha']:
                l = random.choice(range(0,len(board)))
            else:
                validationL = True
    food = {'Coluna': c, 'Linha': l}
    return food