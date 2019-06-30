from Pieces import Pawns, Rooks, Bishops, Knights, Queen, King, Pieces, BoardPiece

class Player:
    pieceIndex = {" ": "Pawns", "R": "Rooks", "B": "Bishops", "N": "Knights", "Q": "Queen", "K": "King"}

    def __init__(self, color, board):
        self.color = color
        self.board = board
        self.grid = self.board.grid
        colorIndex = {"w": 1, "b": -1, "n": 0}
        for c, val in colorIndex.items():
            if val == -(colorIndex[self.color]):
                self.oppColor = c

    def do(self):
        legal = False

        while (legal == False):
            move = input("Your move: ")
            decoded = []
            for i in move:
                decoded.append(i)

            pieces = []
            for j in self.grid:
                if j.__class__.__name__ == self.pieceIndex[decoded[0]] and j.color == self.color:
                    for n in j.moves():
                        if n == decoded[1] + decoded[2]:
                            pieces.append(j)
                            legal = True

            if legal == False:
                print "Illegal Move, try again"

        pieces[0].moveTo(decoded[1], int(decoded[2]))
        print pieces[0].x, pieces[0].y
