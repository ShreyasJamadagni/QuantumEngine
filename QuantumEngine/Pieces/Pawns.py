from Pieces import Pieces
# import Board

class Pawns(Pieces):
    # board = Board.Board()
    prevx = None
    nextx = None
    oppColor = ""
    value = 1
    prevMoves = []
    movement = {"w": 1, "b": -1}

    def __init__(self, color, x, y, grid):
        Pieces.__init__(self, x, y, color, grid)
        self.prevx = self.revWidth.get(self.width.get(self.x)-1)
        self.nextx = self.revWidth.get(self.width.get(self.x)+1)

    def moves(self):
        for c, val in self.colorIndex.items():
            if val == -(self.colorIndex[self.color]):
                self.oppColor = c

        possibleMoves = []
        if self.y+self.movement[self.color] < 9:

            if (self.grid[self.chesstogrid(self.x, self.y+self.movement[self.color])].color == "n" ):
                possibleMoves.append(self.x + str(self.height[self.y+self.movement[self.color]-1]))

            if (len(self.prevMoves) == 0 and self.grid[self.chesstogrid(self.x, self.y+(2*self.movement[self.color]))].color == "n" and self.grid[self.chesstogrid(self.x, self.y+self.movement[self.color])].color == "n"):
                possibleMoves.append(self.x + str(self.height[self.y+(2*self.movement[self.color])-1]))

            #to kill on diagonal to the left
            if (self.prevx != None and self.grid[self.chesstogrid(self.prevx, self.y+self.movement[self.color])].color == self.oppColor):
                print self.prevx
                possibleMoves.append(self.x + self.prevx + str(self.height[self.y+self.movement[self.color]-1]))

            # to kill on the diagonal to the right
            if (self.nextx != None and self.grid[self.chesstogrid(self.nextx, self.y+self.movement[self.color])].color == self.oppColor):
                print self.nextx
                possibleMoves.append(self.x + self.nextx + str(self.height[self.y+self.movement[self.color]-1]))

        return possibleMoves
