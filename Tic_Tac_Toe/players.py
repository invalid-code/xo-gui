import random as rd

from PySimpleGUI import Window
from .ai import minimax


class Player:
    xo = ("X", "O")
    names = ("player", "opponent")

    def __init__(self):
        self.player = rd.choice(Player.xo)
        self.opponent = Player.xo[0] if self.player == Player.xo[1] else Player.xo[1]

    def __str__(self) -> str:
        return f"{self.player}"


class PlayerA(Player):
    name = Player.names[0]

    def __init__(self):
        super().__init__()

    def __repr__(self) -> str:
        return f"Player(player='{self.player}')"

    def play(self, event: str, game, window: Window):
        # self.turn()
        ind = int(event[5])
        if event[1:5] == "CELL":
            game.set_cell([(ind - 1, self.player)])
            window[event].update(self.player)
        return event


class PlayerB(Player):
    name = Player.names[1]

    def __init__(self):
        super().__init__()

    def __repr__(self) -> str:
        return f"Opponent(player='{self.opponent}')"

    def play(self, game, window: Window) -> None:
        # ! not yet correctly implemented minimax alg
        move = minimax(game)
        window[f"-CELL{move}-"].update(self.opponent)
