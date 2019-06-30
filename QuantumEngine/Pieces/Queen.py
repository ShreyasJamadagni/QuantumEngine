# from board import Board
from Pieces import Pieces

class Queen(Pieces):
    # board = Board()
    prevMoves = []
    nextX = []
    prevX = []
    value = 9

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
        while i > 0: # 0 since a would not have a prev x
            prevX.append(self.revWidth[i - 1])
            i = i - 1

        self.nextX = nextX
        self.prevX = prevX

        #bottom right diagonal
        i = self.width[self.x]
        for d in self.nextX:
            if self.y -self.width[d]+i >= 1 and self.grid[self.chesstogrid(d, self.y - (self.width[d] - i))].color != self.color:
                possibleMoves.append(d + str(self.y - (self.width[d] - i)))

            if self.y -self.width[d]+i < 1 or self.grid[self.chesstogrid(d, self.y - (self.width[d] - i))].color != "n":
                break

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

        #Top left diagonal
        i = self.width[self.x]
        for b in self.prevX:
            if self.y - (self.width[b] - i) <= 8 and self.grid[self.chesstogrid(b, self.y - (self.width[b] - i))].color != self.color:
                possibleMoves.append(b + str(self.y - (self.width[b] - i)))

            if self.y - (self.width[b]-i) > 8 or self.grid[self.chesstogrid(b, self.y - (self.width[b] - i))].color != "n":
                break

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
