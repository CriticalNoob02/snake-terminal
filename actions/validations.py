#
def EndBody(worm):
    """Verificação de corpo
        --
        Função responsável por verificar se o próximo movimento pode ser as coordenasdas do seu próprio corpo.

        retorna `validação = {'Up': True, 'Right': True, 'Bottom': True, 'Left': True}`
    """
    l = worm[0]['Linha']
    c = worm[0]['Coluna']

    validation = {'Up': True, 'Right': True, 'Bottom': True, 'Left': True}
    
    up = {'Coluna':c-1 ,'Linha':l }
    right = {'Coluna':c ,'Linha': l+1 }
    bottom = {'Coluna':c+1 ,'Linha': l }
    left = {'Coluna':c ,'Linha': l-1 }

    for i in range(len(worm)):
        if worm[i] == up:
            validation['Up'] = False
        elif worm[i] == right:
            validation['Right'] = False
        elif worm[i] == bottom:
            validation['Bottom'] = False
        elif worm[i] == left:
            validation['Left'] = False
        else:
            pass
    
    return validation
#
def EndBoard(worm,board):
    """Verificação de tabuleiro
        --
        Função responsável por verificar se o próximo movimento pode ser o fim do tabuleiro.

        retorna `validação = {'Up': True, 'Right': True, 'Bottom': True, 'Left': True}`
    """
    l = worm[0]['Linha']
    c = worm[0]['Coluna']
    
    extreme = len(board)

    validation = {'Up': True, 'Right': True, 'Bottom': True, 'Left': True}

    if c <= 0:
        validation['Up'] = False
    elif l >= (extreme-1):
        validation['Right'] = False
    elif c >= (extreme-1):
        validation['Bottom'] = False
    elif l <= 0:
        validation['Left'] = False
    else:
        pass

    return validation
#
def Feeding(worm, food):
    """Verificação de comida
        --
        Função responsável por verificar se o próximo movimento pode ser um alimento.

        retorna `validação = {'Up': True, 'Right': True, 'Bottom': True, 'Left': True}`
    """
    l = worm[0]['Linha']
    c = worm[0]['Coluna']

    up = {'Coluna':c-1 ,'Linha':l }
    right = {'Coluna':c ,'Linha': l+1 }
    bottom = {'Coluna':c+1 ,'Linha': l }
    left = {'Coluna':c ,'Linha': l-1 }

    validation = {'Up': True, 'Right': True, 'Bottom': True, 'Left': True}

    if up == food:
        validation['Up'] = False
    elif right == food:
        validation['Right'] = False
    elif bottom == food:
        validation['Bottom'] = False
    elif left == food:
        validation['Left'] = False
    else:
        pass

    return validation