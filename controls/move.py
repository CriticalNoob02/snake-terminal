from actions.actions import *
from exibition.exibition import Console
from actions.validations import *
from config.config import GenerationFood

def Left(worm, food, board):
    """Movimentação para esquerda
        --
        Compilado de funcionalidade que move a minhoca no terminal.

        retorna: `worm, food`
    """
    end = True
    validation = EndBoard(worm, board)
    
    if validation['Left'] == False:
        end = False

    validation = EndBody(worm)
    if validation['Left'] == False:
        end = False
    
    validation = Feeding(worm, food)
    if validation['Left'] == False:
        worm = Food(worm)
        food = GenerationFood(board, worm)

    worm = MoveLeft(worm)
    worm = Remove(worm)
    Console(board, worm, food, end)

    return worm, food
#
def Right(worm, food, board):
    """Movimentação para direita
        --
        Compilado de funcionalidade que move a minhoca no terminal.

        retorna: `worm, food`
    """
    end = True
    validation = EndBoard(worm, board)
    
    if validation['Right'] == False:
        end = False

    validation = EndBody(worm)
    if validation['Right'] == False:
        end = False
    
    validation = Feeding(worm, food)
    if validation['Right'] == False:
        worm = Food(worm)
        food = GenerationFood(board, worm)

    worm = MoveRight(worm)
    worm = Remove(worm)
    Console(board, worm, food, end)

    return worm, food
#
def Up(worm, food, board):
    """Movimentação para cima
        --
        Compilado de funcionalidade que move a minhoca no terminal.

        retorna: `worm, food`
    """
    end = True
    validation = EndBoard(worm, board)
    if validation['Up'] == False:
        end = False

    validation = EndBody(worm)
    if validation['Up'] == False:
        end = False
    
    validation = Feeding(worm, food)
    if validation['Up'] == False:
        worm = Food(worm)
        food = GenerationFood(board, worm)

    worm = MoveUp(worm)
    worm = Remove(worm)
    Console(board, worm, food, end)

    return worm, food
#
def Bottom(worm, food, board):
    """Movimentação para baixo
        --
        Compilado de funcionalidade que move a minhoca no terminal.

        retorna: `worm, food`
    """
    end = True
    validation = EndBoard(worm, board)
    
    if validation['Bottom'] == False:
        end = False

    validation = EndBody(worm)
    if validation['Bottom'] == False:
        end = False
    
    validation = Feeding(worm, food)
    if validation['Bottom'] == False:
        worm = Food(worm)
        food = GenerationFood(board, worm)

    worm = MoveBottom(worm)
    worm = Remove(worm)
    Console(board, worm, food, end)

    return worm, food
#