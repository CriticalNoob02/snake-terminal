from controls.move import *
from config.config import *
from exibition.exibition import Console
from actions.validations import *

print('Digite o tamanho do board')
value = int(input())

# Configurando game;
mesa = Board(value)
minhoca = Worm()
comida = GenerationFood(mesa,minhoca)
Console(mesa, minhoca, comida)

algo = False

while not algo:
    try:
        value = input().strip()
        match value:
            case 'a':
                minhoca, comida = Left(minhoca, comida, mesa)
            case 'w':
                minhoca, comida = Up(minhoca, comida, mesa)
            case 'd':
                minhoca, comida = Right(minhoca, comida, mesa)
            case 's':
                minhoca, comida = Bottom(minhoca, comida, mesa)
            case _:
                print('Errou')
    except:
        print('Game Over - Perdeu playboy')
        break
#