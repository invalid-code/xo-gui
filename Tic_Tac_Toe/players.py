"""players module"""

import random as rd

from PySimpleGUI import Window

from .ai import minimax


class Player:
    xo = ("X", "O")
    name = "player"

    def __init__(self):
        self.player = rd.choice(Player.xo)

    def __str__(self) -> str:
        return f"player: {self.player}\n".title()

    def __repr__(self) -> str:
        return f"Player(player='{self.player}')"

    def play(self, event: str, game, window: Window) -> None:
        ind = int(event[5])
        game.set_cell([(ind - 1, self.player)])
        window[event].update(self.player)
        window.refresh()
        game.turn()


class Opponent:
    name = "opponent"

    def __init__(self, player: Player):
        self.opponent = (
            Player.xo[0] if player.player == Player.xo[1] else Player.xo[1]
        )

    def __str__(self) -> str:
        return f"opponent: {self.opponent}\n".title()

    def __repr__(self) -> str:
        return f"Opponent(opponent='{self.opponent}')"

    def play(self, game, window: Window) -> None:
        game.turn()
        move = minimax(game)
        game.set_cell([(move, self.opponent)])
        window[f"-CELL{move + 1}-"].update(self.opponent)
        window.refresh()
