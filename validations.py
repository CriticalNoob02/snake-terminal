#
def EndBody(worm):
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
    l = worm[0]['Linha']
    c = worm[0]['Coluna']
    
    extreme = len(board)

    validation = {'Up': True, 'Right': True, 'Bottom': True, 'Left': True}

    if worm[0]['Coluna'] <= 0:
        validation['Up'] = False
    elif worm[0]['Linha'] >= extreme:
        validation['Right'] = False
    elif worm[0]['Coluna'] >= extreme:
        validation['Bottom'] = False
    elif worm[0]['Linha'] <= 0:
        validation['Left'] = False
    else:
        pass

    return validation