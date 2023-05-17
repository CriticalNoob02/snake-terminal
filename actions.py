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

    c -= 1  # movimento para esquerda;

    worm.insert(0,{'Coluna': c, 'Linha': l})

    return worm
#
def Remove(worm):
    worm.pop(-1)
    
    return worm
#