from Board import Board
from Engine import Engine
from Player import Player

def main():
    board = Board()
    Player = Player()
    Engine = Engine("b", board)
    finished = False

    while (finished == False):
        Player.do(move=input('Your move: '))
