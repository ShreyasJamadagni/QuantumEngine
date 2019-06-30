from collections import OrderedDict

class Pieces(object):
    width = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    height = [1, 2, 3, 4, 5, 6, 7, 8]
    revWidth = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
    grid = []
    colorIndex = {"w": 1, "b": -1, "n": 0}
    oppColor = ""

    def gridtochess(self, n):
        x3 = ""
        d = 64-n
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

    def moveTo(self, x, y):
        self.x = x
        self.y  = y

    def __init__(self, x, y, color, grid):
        self.x = x
        self.y = y
        self.color = color
        self.grid = grid

        for c, val in self.colorIndex.items():
            if val == -(self.colorIndex[self.color]):
                self.oppColor = c
