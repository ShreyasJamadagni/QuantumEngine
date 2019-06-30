from Pieces import Pieces
# from .. import Board

class King(Pieces):
    # board = Board()
    prevMoves = []

    def __init__(self, color, x, y, grid):
        Pieces.__init__(self, x, y, color, grid)

    #All the places the king can go, be it illegal or not
    def uncheckedmoves(self):
        possibleMoves = []
        nextx = ""
        prevx = ""

        for x, val in self.width.items():
            if val == self.width.get(self.x) - 1:
                prevx = x # prevx = "" if prevx does not exist

            if val == self.width.get(self.x) + 1:
                nextx = x # nextx = "" if nextx does not exist

        if self.y + 1 < 9 and self.grid[self.chesstogrid(self.x, self.y + 1)].color != self.color:
            possibleMoves.append(self.x + str(self.y+1))
        if self.y - 1 > 0 and self.grid[self.chesstogrid(self.x, self.y - 1)].color != self.color:
            possibleMoves.append(self.x + str(self.y-1))
        if nextx != "" and self.grid[self.chesstogrid(nextx, self.y)].color != self.color:
            possibleMoves.append(nextx + str(self.y))
        if prevx != "" and self.grid[self.chesstogrid(prevx, self.y)].color != self.color:
            possibleMoves.append(prevx + str(self.y))
        if prevx != "" and self.y + 1 <=8 and self.grid[self.chesstogrid(prevx, self.y+1)].color != self.color:
            possibleMoves.append(prevx + str(self.y+1))
        if nextx != "" and self.y + 1 <=8 and self.grid[self.chesstogrid(nextx, self.y+1)].color != self.color:
            possibleMoves.append(nextx + str(self.y+1))
        if prevx != "" and self.y - 1 >= 1 and self.grid[self.chesstogrid(prevx, self.y-1)].color != self.color:
            possibleMoves.append(prevx + str(self.y-1))
        if nextx != "" and self.y - 1 >= 1 and self.grid[self.chesstogrid(nextx, self.y-1)].color != self.color:
            possibleMoves.append(nextx + str(self.y-1))

        return possibleMoves

    #Prevention of illegal moves.
    def moves():
        possibleMoves = uncheckedmoves()
        illegalMoves = []
        for j in self.grid:
            if j.color == self.oppColor and j.__class__.__name__ != "King":
                illegalMoves = illegalMoves + j.moves()
            elif j.color == self.oppColor and j.__class__.__name__ == "King":
                illegalMoves = illegalMoves + j.uncheckedmoves()
    #Between two kings the illegal region is the same, therefore where ever both kings uncheckedmoves overlap, thats the illegal region
    #Thats the definition of an illegal move- where two kings' possibleMoves overlap

        print illegalMoves
        for i in illegalMoves:
            for j in possibleMoves:
                if j == i:
                    possibleMoves.remove(j)

        return possibleMoves
