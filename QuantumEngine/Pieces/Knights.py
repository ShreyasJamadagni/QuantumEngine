# from board import Board
from Pieces import Pieces

class Knights(Pieces):
    # board = Board()
    prevx = None
    nextx = None
    prev2x = None
    next2x = None
    prevMoves = []
    value = 3
    n = 4
    possibleMoves = []

    def moves(self):
        j = []
        self.prevx = self.revWidth.get(self.width.get(self.x)-1)
        self.nextx = self.revWidth.get(self.width.get(self.x)+1)
        self.prev2x = self.revWidth.get(self.width.get(self.x)-2)
        self.next2x = self.revWidth.get(self.width.get(self.x)+2)

        if self.prevx != None and self.y - 2 > 0:
            j.append((self.prevx , str(self.y - 2)))

        if self.prevx != None and self.y + 2 < 9:
            j.append((self.prevx , str(self.y + 2)))

        if self.nextx != None and self.y - 2 > 0:
            j.append((self.nextx , str(self.y - 2)))

        if self.nextx != None and self.y + 2 < 9:
            j.append((self.nextx , str(self.y + 2)))

        if self.next2x != None and self.y + 1 < 9:
            j.append((self.next2x , str(self.y + 1)))

        if self.next2x != None and self.y - 1 > 0:
            j.append((self.next2x , str(self.y - 1)))

        if self.prev2x != None and self.y + 1 < 9:
            j.append((self.prev2x , str(self.y + 1)))

        if self.prev2x != None and self.y - 1 > 0:
            j.append((self.prev2x , str(self.y - 1)))

        for g in j:
            if self.grid[self.chesstogrid(g[0], int(g[1]))].color == self.color:
                j.remove(g)

        l = 0
        while l < len(j):
            q = j[l][0] + j[l][1]
            j[l] = q
            l = l + 1

        self.possibleMoves = j

        return self.possibleMoves

    def __init__(self, color, x, y, grid):
        Pieces.__init__(self, x, y, color, grid)
