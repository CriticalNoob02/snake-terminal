from actions.actions import *
from exibition.exibition import Console
from actions.validations import *

def Left(worm, food, board):
    validation = EndBoard(worm, board)
    if validation['Left'] == False:
        pass

    validation = EndBody(worm)
    if validation['Left'] == False:
        pass
    
    validation = Feeding(worm, food)
    if validation['Left'] == False:
        worm = Food(worm)
        return worm

    worm = MoveLeft(worm)
    worm = Remove(worm)
    Console(board, worm, food)

    return worm
#
def Right(worm, food, board):
    validation = EndBoard(worm, board)
    if validation['Right'] == False:
        pass

    validation = EndBody(worm)
    if validation['Right'] == False:
        pass
    
    validation = Feeding(worm, food)
    if validation['Right'] == False:
        worm = Food(worm)
        return worm

    worm = MoveRight(worm)
    worm = Remove(worm)
    Console(board, worm, food)

    return worm
#
def Up(worm, food, board):
    validation = EndBoard(worm, board)
    if validation['Up'] == False:
        pass

    validation = EndBody(worm)
    if validation['Up'] == False:
        pass
    
    validation = Feeding(worm, food)
    if validation['Up'] == False:
        worm = Food(worm)
        return worm

    worm = MoveUp(worm)
    worm = Remove(worm)
    Console(board, worm, food)

    return worm
#
def Bottom(worm, food, board):
    validation = EndBoard(worm, board)
    if validation['Bottom'] == False:
        pass

    validation = EndBody(worm)
    if validation['Bottom'] == False:
        pass
    
    validation = Feeding(worm, food)
    if validation['Bottom'] == False:
        worm = Food(worm)

    worm = MoveBottom(worm)
    worm = Remove(worm)
    Console(board, worm, food)

    return worm
#