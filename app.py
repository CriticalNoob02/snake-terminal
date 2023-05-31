from controls.move import *
from config.config import *
from exibition.exibition import Console
from actions.validations import *
import threading 

tamanho = int(input('\n Digite o tamanho do board: '))

# Configurando jogo;
jogo = True
tempo_limite = 2
default = 'd'
mesa = Board(tamanho)
minhoca = Worm()
comida = GenerationFood(mesa,minhoca)
Console(mesa, minhoca, comida)

#
def InputMove():
    global value 
    value = input()  
#

while jogo:
    try:
        value = ''
        leitor = threading.Thread(target=InputMove)

        leitor.start()
        leitor.join(tempo_limite)
        
        if leitor.is_alive():
            value = default
            pass
        else: 
            print(value)
            pass

        match value:
            case 'a':
                minhoca, comida = Left(minhoca, comida, mesa)
                default = 'a'
            case 'w':
                minhoca, comida = Up(minhoca, comida, mesa)
                default = 'w'
            case 'd':
                minhoca, comida = Right(minhoca, comida, mesa)
                default = 'd'
            case 's':
                minhoca, comida = Bottom(minhoca, comida, mesa)
                default = 's'
            case _:
                print('Errou'+ value)
    except:
        print('Game Over - Perdeu playboy')
        jogo = False
        break
