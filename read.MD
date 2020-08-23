
*Establish a Search Tree --minimax
**Use a neural Network To Prune a search Tree

***Value network : int v = f(state) -- state(board)

Pieces (x2):
 - blank
 - pawn (8)
 - bishop (2)
 - knight (2)
 - rook (2)
 - queen (1)
 - king (1)

Board States:

Extra Board States (4):
 - en passant: special pawn capture after pawn moves from start
                    kill from behind
 - king unmoved: allows to do special move with rook

total states:
 8 x 8 x 4 + 4(extra states)= 260 bits
