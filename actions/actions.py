#
def Food(worm):
    """Comer alimento
        --
        Função responsável por aumentar o corpo da minhoca adicionando as coordenadas iniciais.

        retorna: `worm`
    """
    worm.append({'Coluna': 0, 'Linha': 0})
    return worm
#
def MoveRight(worm):
    """Mover para direita
        --
        Função responsável por mudar as coordenadas da ultima peça da minhoca para a direita.

        retorna: `worm`
    """
    c = worm[0]['Coluna']
    l = worm[0]['Linha']

    l += 1  # movimento para esquerda;

    worm.insert(0,{'Coluna': c, 'Linha': l})

    return worm
#
def MoveBottom(worm):
    """Mover para baixo
        --
        Função responsável por mudar as coordenadas da ultima peça da minhoca para baixo.

        retorna: `worm`
    """
    c = worm[0]['Coluna']
    l = worm[0]['Linha']

    c += 1  # movimento para esquerda;

    worm.insert(0,{'Coluna': c, 'Linha': l})

    return worm
#
def MoveLeft(worm):
    """Mover para esquerda
        --
        Função responsável por mudar as coordenadas da ultima peça da minhoca para a esquerda.

        retorna: `worm`
    """
    # TODO: Criar uma validação para o movimento não ser em uma coordenada que a cobra já exista
    c = worm[0]['Coluna']
    l = worm[0]['Linha']

    l -= 1  # movimento para direita;

    worm.insert(0,{'Coluna': c, 'Linha': l})

    return worm
#
def MoveUp(worm):
    """Mover para cima
        --
        Função responsável por mudar as coordenadas da ultima peça da minhoca para a cima.
    
        retorna: `worm`
    """
    c = worm[0]['Coluna']
    l = worm[0]['Linha']

    c -= 1  # movimento para esquerda;

    worm.insert(0,{'Coluna': c, 'Linha': l})

    return worm
#
def Remove(worm):
    """Remover coordenadas
        --
        Função responsável por remover a parte final do corpo da minhoca.

        retorna: `worm`
    """
    worm.pop(-1)
    
    return worm
#