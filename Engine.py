from Board import Board
from Pieces import Pawns, Rooks, Bishops, Knights, Queen, King, Pieces, BoardPiece

class Engine:
    def __init__(self, color, board):
        self.color = color
        self.board = board
        self.grid = self.board.grid
        colorIndex = {"w": 1, "b": -1, "n": 0}
        for c, val in colorIndex.items():
            if val == -(colorIndex[self.color]):
                self.oppColor = c

    def outcome(self, target):
        pos = target.x + str(target.y)
        sequence = []

        protection = 0
        protectors = []
        totalValueProtecting = 0

        attack = 0
        attackers = []
        totalValueAttacking = 0

        for i in self.grid:
            if i.color == piece.color:
                for v in i.moves():
                    if v == pos:
                        protection += 1
                        totalValueProtecting += i.value
                        protectors.append(i)

            if i.color == piece.oppColor:
                for c in i.moves():
                    if c == pos
                        attack += 1
                        totalValueAttacking += i.value
                        attackers.append(i)

        attackers1 = attackers
        i = 0
        while (i < len(attackers)):
            lowest = attackers1[0].value
            for h in attackers:
                if h.value < lowest:
                    sequence.append(h.__class__.__name__ + "x" + pos)
                    attackers1.remove(h)
            i += 1

        if (attack > protection and totalValueProtecting > totalValueAttacking):
            return [True, totalValueProtecting - totalValueAttacking, sequence[0]]


    def recommendedCapture(self):
        sequence = ""
        highestdeficit = 0
        for i in self.grid:
            if i.color == self.oppColor:
                if capture(i)[0] == True and capture(i)[1] > highestdeficit:
                    highestdeficit = capture(i)[1]
                    sequence = capture(i)[2]

        return sequence

    def do(self):
        recommendedCapture = recomendedCapture()
        recomCap = []
        piece = []
        for b in self.grid:
            if b.__class__.__name__ == recomCap[0]:
                for g in b.moves():
                    if g == recomCap[1] + recomCap[2]:
                        piece.append(g)

        piece[0].moveTo(recomCap[1], int(recomCap[2]))
        print(recommendedCapture)
