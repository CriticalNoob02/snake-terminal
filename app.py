from actions import *
from config import *
from exibition import *

# Configurando game;
mesa = Board(6)
minhoca = Worm()

# iniciando;
Console(mesa, minhoca)

# Movimento horizontal;
minhoca = MoveLeft(minhoca)
minhoca = Remove(minhoca)
Console(mesa, minhoca)

# Alimentando minhoca;
minhoca  = Food(minhoca)
minhoca = MoveLeft(minhoca)
minhoca = Remove(minhoca)
Console(mesa, minhoca)

minhoca = MoveLeft(minhoca)
minhoca = Remove(minhoca)
Console(mesa, minhoca)

# Alimentando minhoca;
minhoca = Food(minhoca, )
minhoca = MoveLeft(minhoca)
minhoca = Remove(minhoca)
Console(mesa, minhoca)

# movendo pra baixo;
minhoca = MoveBottom(minhoca)
minhoca = Remove(minhoca)
Console(mesa, minhoca)

minhoca = MoveBottom(minhoca)
minhoca = Remove(minhoca)
Console(mesa, minhoca)

minhoca = Food(minhoca)
minhoca = MoveBottom(minhoca)
minhoca = Remove(minhoca)
Console(mesa, minhoca)

minhoca = MoveBottom(minhoca)
minhoca = Remove(minhoca)
Console(mesa, minhoca)

minhoca = MoveLeft(minhoca)
minhoca = Remove(minhoca)
Console(mesa, minhoca)





# minhoca = MoveLeft(minhoca)

# posição,mesa = MoveBottom(posição, mesa)
# mesa = RemoveLeft(minhoca, posição, mesa)
# Console(mesa)
# print(posição)