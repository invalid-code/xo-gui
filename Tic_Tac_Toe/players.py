from .ai import minimax


class Player:
    def __init__(self, game, player_avatar: str, name: str):
        self.game = game
        self.player = player_avatar
        self.name = name  # to know who is the player and the opponent(ai)

    def __repr__(self) -> str:
        return f"Player(player='{self.player}', name='{self.name}')"

    def __str__(self) -> str:
        return f"player is {self.player}\nplayer is the {self.name}"


class PlayerA(Player):
    def play(self, event: str) -> str:
        self.game.turn()
        ind = int(event[5])
        if event[1:5] == "CELL":
            self.game.set_cell([(ind, self.player)])
            return event


class PlayerB(Player):
    def play(self) -> None:
        # ! not yet correctly implemented minimax alg
        self.game.turn()
        move = minimax(self.game)
