import random as rd
import copy as cp

import PySimpleGUI as sg


def minimax(game, window: sg.Window):
    game = cp.deepcopy(game)
    decision_tree = []
    # player_row = []
    opponent_row = []

    if not game.finished_game(window):
        return {"score": 0}
    winner = game.check_winner(window)
    if winner:
        if winner.get("winner") == "player":
            return {"score": -1}
        if winner.get("winner") == "opponent":
            return {"score": 1}

    for key, cell in game.table.items(): # loop through all cells
        if game.check_cell(key):  # if cell is empty
            game.table.update({key: game.opponent.player})
            opponent_row.append(game.table)
            print(game.table)
            minimax(game, window)

    decision_tree.append(opponent_row)
    print(decision_tree)


class Player:
    def __init__(self, player_avatar: str, is_player_opponent: str):
        self.player = player_avatar
        self.is_player_opponent = (
            is_player_opponent  # to know who is the player and the opponent(ai)
        )

    def __repr__(self) -> str:
        return f"Player(player={self.player}, is_player_opponent={self.is_player_opponent})"

    def __str__(self) -> str:
        return f"player is {self.player}\nplayer is the {self.is_player_opponent}"


class PlayerA(Player):
    def play(self, game, window: sg.Window, event: str):
        ind = event[5]
        if event[1:5] == "CELL":
            game.table[ind] = self.player
            window[f"-CELL{ind}-"].update(self.player)


class PlayerB(Player):
    def play(self, game, window: sg.Window):
        move = minimax(game, window)


class Game:
    xo = ("X", "O")

    def __init__(self):
        self.player_avatar = rd.choice(Game.xo)
        self.player = PlayerA(self.player_avatar, "player")
        if self.player_avatar == "X":
            self.opponent = PlayerB("O", "opponent")
        else:
            self.opponent = PlayerB("X", "opponent")
        self.first = rd.choice(Game.xo)
        self.table = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": "",
            "9": "",
        }

    def __repr__(self) -> str:
        return f"Game(player_avatar={self.player_avatar}, player={self.player.__repr__()}, opponent={self.opponent.__repr__()}, first={self.first}, table={self.table})"

    def __str__(self) -> str:
        return f"the player's avatar will be {self.player_avatar}\nplayer will be {self.player}\nopponent will be {self.opponent}\n {self.player if self.first else self.opponent}\n {self.table} will be playing field"

    def get_cell_value(self, ind: str) -> str | None:
        return self.table.get(ind)

    def is_player_first(self) -> bool:
        if self.first == self.player.player:
            return True
        return False

    def finished_game(self, window: sg.Window) -> bool:
        """To check if all cells are filled"""

        for cell in self.table.values():

            if cell not in Game.xo:  # if a cell has no value return true
                return True

        window["-POPUP-"].update("Tie")
        window["-RETRY-"].update(visible=True)
        return False

    def check_cell(self, ind: str) -> bool:
        """check if cell is already taken"""

        if self.table.get(ind) not in Game.xo:
            return True
        return False

    def check_winner(self, window: sg.Window) -> dict[str, str] | None:
        player = self.player
        opponent = self.opponent

        if (
            self.table.get(str(1)) == player.player
            and self.table.get(str(1 + 1)) == player.player
            and self.table.get(str(1 + 2)) == player.player
            or self.table.get(str(1)) == player.player
            and self.table.get(str(1 + 3)) == player.player
            and self.table.get(str(1 + 6)) == player.player
            or self.table.get(str(1)) == player.player
            and self.table.get(str(1 + 4)) == player.player
            and self.table.get(str(1 + 8)) == player.player
            or self.table.get(str(9)) == player.player
            and self.table.get(str(9 - 1)) == player.player
            and self.table.get(str(9 - 2)) == player.player
            or self.table.get(str(9)) == player.player
            and self.table.get(str(9 - 3)) == player.player
            and self.table.get(str(9 - 6)) == player.player
            or self.table.get(str(5)) == player.player
            and self.table.get(str(5 - 3)) == player.player
            and self.table.get(str(5 + 3)) == player.player
            or self.table.get(str(5)) == player.player
            and self.table.get(str(5 - 1)) == player.player
            and self.table.get(str(5 + 1)) == player.player
            or self.table.get(str(5)) == player.player
            and self.table.get(str(5 - 2)) == player.player
            and self.table.get(str(5 + 2)) == player.player
        ):
            window["-POPUP-"].update("You win")
            window["-RETRY-"].update(visible=True)
            return {"winner": player.is_player_opponent}
        if (
            self.table.get(str(1)) == opponent.player
            and self.table.get(str(1 + 1)) == opponent.player
            and self.table.get(str(1 + 2)) == opponent.player
            or self.table.get(str(1)) == opponent.player
            and self.table.get(str(1 + 3)) == opponent.player
            and self.table.get(str(1 + 6)) == opponent.player
            or self.table.get(str(1)) == opponent.player
            and self.table.get(str(1 + 4)) == opponent.player
            and self.table.get(str(1 + 8)) == opponent.player
            or self.table.get(str(9)) == opponent.player
            and self.table.get(str(9 - 1)) == opponent.player
            and self.table.get(str(9 - 2)) == opponent.player
            or self.table.get(str(9)) == opponent.player
            and self.table.get(str(9 - 3)) == opponent.player
            and self.table.get(str(9 - 6)) == opponent.player
            or self.table.get(str(5)) == opponent.player
            and self.table.get(str(5 - 3)) == opponent.player
            and self.table.get(str(5 + 3)) == opponent.player
            or self.table.get(str(5)) == opponent.player
            and self.table.get(str(5 - 1)) == opponent.player
            and self.table.get(str(5 + 1)) == opponent.player
            or self.table.get(str(5)) == opponent.player
            and self.table.get(str(5 - 2)) == opponent.player
            and self.table.get(str(5 + 2)) == opponent.player
        ):
            window["-POPUP-"].update("You lose")
            window["-RETRY-"].update(visible=True)
            return {"winner": opponent.is_player_opponent}
