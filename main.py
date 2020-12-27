from Game.Game import Game
import sys
import json


if __name__ == '__main__':
    sys_list = sys.argv
    g = list()
    with open(sys_list[1], "r") as f:
        g = json.load(f)
    for i in g:
        game = Game(i)
        print("Game")
        for j in i:
            print(j)
        print(f"Неш:{game.play()}")