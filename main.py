 #!/usr/bin/env python

from Board import Board
from Engine import Engine
from Player import Player

def main():
    board = Board()
    Player = Player("w", board)
    Engine = Engine("b", board)
    finished = False

    while (finished == False):
        Player.do(move=input('Your move: '))
        Engine.do()
        finished = Board.check()
