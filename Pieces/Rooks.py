# from .board import Board
from Pieces import Pieces

class Rooks(Pieces):
    # board = Board()
    prevMoves = []
    value = 5

    def __init__(self, color, x, y, grid):
        Pieces.__init__(self, x, y, color, grid)

    def moves(self):
        possibleMoves = []

        # forward direction
        i = self.y + 1
        while i <= len(self.height) - 1:
            if self.grid[self.chesstogrid(self.x, i)].color != self.color:
                possibleMoves.append(self.x + str(i))
            if self.grid[self.chesstogrid(self.x, i)].color != "n":
                break
            i = i + 1

        # Backward direction
        i = self.y - 1
        while i >= 1:
            if self.grid[self.chesstogrid(self.x, i)].color != self.color:
                possibleMoves.append(self.x + str(i))
            if self.grid[self.chesstogrid(self.x, i)].color != "n": #if the piece is either white or black, it cannot continue going back
                break
            i = i - 1

        # Left
        i = self.chesstogrid(self.x, self.y) - 1
        while i >= 8*(self.y - 1):
            if self.grid[i].color != self.color:
                possibleMoves.append(self.gridtochess(i)[0] + str(self.y))
            if self.grid[i].color != "n": #if the piece is either white or black, it cannot continue going left
                break
            i = i - 1

        # Right
        i = self.chesstogrid(self.x, self.y)+1
        while i <= (8*self.y) - 1:
            if self.grid[i].color != self.color:
                possibleMoves.append(self.gridtochess(i)[0] + str(self.y))
            if self.grid[i].color != "n":
                break
            i = i + 1

        return possibleMoves
