import random
#
def Food(worm):
    # TODO: Criar um gerador de localização da comida
    worm.append({'Coluna': 0, 'Linha': 0})
    return worm
#
def MoveLeft(worm):
    c = worm[0]['Coluna']
    l = worm[0]['Linha']

    l += 1  # movimento para esquerda;

    worm.insert(0,{'Coluna': c, 'Linha': l})

    return worm
#
def MoveBottom(worm):
    c = worm[0]['Coluna']
    l = worm[0]['Linha']

    c += 1  # movimento para esquerda;

    worm.insert(0,{'Coluna': c, 'Linha': l})

    return worm
#
def MoveRight(worm):
    # TODO: Criar uma validação para o movimento não ser em uma coordenada que a cobra já exista
    c = worm[0]['Coluna']
    l = worm[0]['Linha']

    l -= 1  # movimento para direita;

    worm.insert(0,{'Coluna': c, 'Linha': l})

    return worm
#
def MoveUp(worm):
    c = worm[0]['Coluna']
    l = worm[0]['Linha']

    c -= 1  # movimento para esquerda;

    worm.insert(0,{'Coluna': c, 'Linha': l})

    return worm
#
def Remove(worm):
    worm.pop(-1)
    
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