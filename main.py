 #!/usr/bin/env python

from Board import Board
from Engine import Engine
from Player import Player

def main():
    board = Board()
    player = Player("w", board)
    engine = Engine("b", board)
    finished = False

    while (finished == False):
        player.do()
        engine.do()
        finished = Board.check()

main()
