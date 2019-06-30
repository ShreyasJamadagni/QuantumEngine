from Pieces import Pieces

class BoardPiece(Pieces):
    def __init__ (self, x, y, grid):
        Pieces.__init__(self, x, y, "n", grid)
