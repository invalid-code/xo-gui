import random as rd

# from .ai import minimax


class Player:
    xo = ("X", "O")
    names = ("player", "opponent")  # to know who is the player and the opponent(ai)

    def __init__(self):
        self.player = rd.choice(Player.xo)
        self.opponent = Player.xo[0] if self.player == Player.xo[1] else Player.xo[1]

    def __str__(self) -> str:
        return f"player is {self.player}"


class PlayerA(Player):
    name = Player.names[0]

    def __init__(self):
        super().__init__()

    def __repr__(self) -> str:
        return f"Player(player='{self.player}'"

    def play(self, event: str) -> str:
        # self.turn()
        # ind = int(event[5])
        # if event[1:5] == "CELL":
        # self.game.set_cell([(ind, self.player)])
        return event


class PlayerB(Player):
    name = Player.names[1]

    def __init__(self):
        super().__init__()

    def __repr__(self) -> str:
        return f"Opponent(player='{self.opponent}'"

    def play(self) -> None:
        # ! not yet correctly implemented minimax alg
        pass
