from Pieces import Pawns, Rooks, Bishops, Knights, Queen, King, Pieces, BoardPiece
from collections import OrderedDict

class Board:
    width = OrderedDict()
    height = [1, 2, 3, 4, 5, 6, 7, 8]
    grid = []

    def check(self):
        kings = []
        for g in self.grid:
            if g.__class__.__name__ == "King":
                kings.append(g)

        for h in kings:
            if len(h.moves()) == 0:
                for n in self.grid:
                    if n.__class__.__name__ != "King":
                        for j in n.moves():
                            if j == h.x + str(h.y):
                                return True
            else:
                return False


    def gridtochess(self, n):
        x3 = ""
        d = 64 - n
        widthVal = int(d % 8)

        if widthVal == 0:
            x3 = "a"
            widthVal = 0
        if widthVal != 0:
            widthVal = 8-widthVal
        for key, val in self.width.items():
            if val == widthVal:
                x3 = key

        y = (n-widthVal)/8 + 1

        return [x3, y]

    def chesstogrid(self, x, y):
        return self.width.get(x) + (8*(y-1))

    def __init__(self):
        words = ["a", "b", "c", "d", "e", "f", "g", "h"]
        i = 0
        while i < 8:
            self.width[words[i]] = i
            i = i + 1

        self.grid.insert(0, Rooks("w", self.gridtochess(0)[0], self.gridtochess(0)[1], self.grid))
        self.grid.insert(1, Knights("w", self.gridtochess(1)[0], self.gridtochess(1)[1], self.grid))
        self.grid.insert(2, Bishops("w", self.gridtochess(2)[0], self.gridtochess(2)[1], self.grid))
        self.grid.insert(3, Queen("w", self.gridtochess(3)[0], self.gridtochess(3)[1], self.grid))
        self.grid.insert(4, King("w", self.gridtochess(4)[0], self.gridtochess(4)[1], self.grid))
        self.grid.insert(5, Bishops("w", self.gridtochess(5)[0], self.gridtochess(5)[1], self.grid))
        self.grid.insert(6, Knights("w", self.gridtochess(6)[0], self.gridtochess(6)[1], self.grid))
        self.grid.insert(7, Rooks("w", self.gridtochess(7)[0], self.gridtochess(7)[1], self.grid))

        i = 8
        while i < 16:
            self.grid.insert(i, Pawns("w", self.gridtochess(i)[0], self.gridtochess(i)[1], self.grid))
            # print(Pieces.gridtochess(i))
            i = i + 1
        while i < 48:
            self.grid.insert(i, BoardPiece(self.gridtochess(i)[0], self.gridtochess(i)[1], self.grid))
            i = i + 1

        while i < 56:
            self.grid.insert(i, Pawns("b", self.gridtochess(i)[0], self.gridtochess(i)[1], self.grid))
            i = i + 1

        self.grid.insert(56, Rooks("b", self.gridtochess(56)[0], self.gridtochess(56)[1], self.grid))
        self.grid.insert(57, Knights("b", self.gridtochess(57)[0], self.gridtochess(57)[1], self.grid))
        self.grid.insert(58, Bishops("b", self.gridtochess(58)[0], self.gridtochess(58)[1], self.grid))
        self.grid.insert(59, Queen("b", self.gridtochess(59)[0], self.gridtochess(59)[1], self.grid))
        self.grid.insert(60, King("b", self.gridtochess(60)[0], self.gridtochess(60)[1], self.grid))
        self.grid.insert(61, Bishops("b", self.gridtochess(61)[0], self.gridtochess(61)[1], self.grid))
        self.grid.insert(62, Knights("b", self.gridtochess(62)[0], self.gridtochess(62)[1], self.grid))
        self.grid.insert(63, Rooks("b", self.gridtochess(63)[0], self.gridtochess(63)[1], self.grid))
