# from board import Board
from Pieces import Pieces

class Bishops(Pieces):
    # board = Board()
    prevMoves = []
    nextX = []
    prevX = []
    value = 3

    def __init__(self, color, x, y, grid):
        Pieces.__init__(self, x, y, color, grid)

    def moves(self):
        possibleMoves = []
        nextX = []
        prevX = []

        i = self.width[self.x]
        while i < 7: # 7 since h would not have a nextx
            nextX.append(self.revWidth[i + 1])
            i = i + 1

        i = self.width[self.x]
        while i > 0: # 1 since a would not have a prev x
            prevX.append(self.revWidth[i - 1])
            i = i - 1

        self.prevX = prevX
        self.nextX = nextX

        #top right diagonal
        i = self.width[self.x]
        for d in self.nextX:
            if self.y +self.width[d]-i <= 8 and self.grid[self.chesstogrid(d, self.y +self.width[d]-i)].color != self.color:
                possibleMoves.append(d + str(self.y +self.width[d]-i))

            if self.y +self.width[d]-i > 8 or self.grid[self.chesstogrid(d, self.y +self.width[d]-i)].color != "n":
                break

        #bottom left diagonal
        i = self.width[self.x]
        for v in self.prevX:
            if self.y + self.width[v] - i >= 1 and self.grid[self.chesstogrid(v, self.y + self.width[v] - i)].color != self.color:
                possibleMoves.append(v + str(self.y + self.width[v] - i))
            if self.y + self.width[v] - i < 1 or self.grid[self.chesstogrid(v, self.y +self.width[v] - i)].color != "n":
                break

        #bottom right diagonal
        i = self.width[self.x]
        for d in self.nextX:
            if self.y -self.width[d]+i >= 1 and self.grid[self.chesstogrid(d, self.y - (self.width[d] - i))].color != self.color:
                possibleMoves.append(d + str(self.y - (self.width[d] - i)))

            if self.y -self.width[d]+i < 1 or self.grid[self.chesstogrid(d, self.y - (self.width[d] - i))].color != "n":
                break

        #top left diagonal
        i = self.width[self.x]
        for b in self.prevX:
            if self.y - (self.width[b] - i) <= 8 and self.grid[self.chesstogrid(b, self.y - (self.width[b] - i))].color != self.color:
                possibleMoves.append(b + str(self.y - (self.width[b] - i)))

            if self.y - (self.width[b]-i) > 8 or self.grid[self.chesstogrid(b, self.y - (self.width[d] - i))].color != "n":
                break

        return possibleMoves
