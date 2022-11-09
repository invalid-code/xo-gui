import random as rd
import copy as cp
import string as str_
import PySimpleGUI as sg


def minimax(
    game,
    window: sg.Window,
    depth=0
) -> dict[str, int] | None:
    game_copy = cp.deepcopy(game)
    decision_tree = []

    player_win = game_copy.win
    opponent_win = game_copy.lose
    # score = 0
    # player_row = []

    # if game.turn_ == game.opponent.name: # is this needed? prob no
    # if not opponent_win(window) or player_win(window):
    while game_copy.tie(window) or opponent_win(window) or player_win(window):
        print(game_copy.format())
        for key, cell in game_copy.table.items():  # loop through all the cells
            if not cell:  # if cell is empty
                branch = cp.deepcopy(game_copy)  # copy the game
                branch.table.update(
                    {key: game.opponent.player}
                )  # update the current empty cell with opponent.player
                decision_tree.append({"game": branch})  # add branch to decision tree
                for (
                    key1,
                    cell1,
                ) in (
                    branch.table.items()
                ):  # loop through all posible player moves after opponent(ai) makes branch
                    if not cell1:  # if cell is empty
                        branch1 = cp.deepcopy(game)  # copy the branch
                        branch1.table.update(
                            {key1: game.player.player}
                        )  # update the current empty cell with player.player
                        decision_tree.append(
                            {"game": branch1}
                        )  # add branch to decision tree

    if player_win(window):
        pass
    if opponent_win(window):
        pass
    if game.tie(window):
        pass


class Player:
    def __init__(self, player_avatar: str, name: str):
        self.player = player_avatar
        self.name = name  # to know who is the player and the opponent(ai)

    def __repr__(self) -> str:
        return f"Player(player={self.player}, name={self.name})"

    def __str__(self) -> str:
        return f"player is {self.player}\nplayer is the {self.name}"


class PlayerA(Player):
    def play(self, game, window: sg.Window, event: str):
        ind = event[5]
        # game.turn(self.name)
        if event[1:5] == "CELL":
            game.table[ind] = self.player
            window[f"-CELL{ind}-"].update(self.player)
            return True


class PlayerB(Player):
    def play(self, game, window: sg.Window):
        # game.turn(self.name)
        move = minimax(game, window)


class Tic_Tac_Toe:
    xo = ("X", "O")

    def __init__(self):
        self.player_avatar = rd.choice(Tic_Tac_Toe.xo)
        self.player = PlayerA(self.player_avatar, "player")
        if self.player_avatar == "X":
            self.opponent = PlayerB("O", "opponent")
        else:
            self.opponent = PlayerB("X", "opponent")
        self.first = rd.choice(Tic_Tac_Toe.xo)
        # self.turn_ = self.first
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
        return f"Tic_Tac_Toe(player_avatar={self.player_avatar}, player={self.player.__repr__()}, opponent={self.opponent.__repr__()}, first={self.first}, table={self.table})"

    def __str__(self) -> str:
        return f"the player's avatar will be {self.player_avatar}\nplayer will be {self.player}\nopponent will be {self.opponent}\n {self.player if self.first else self.opponent}\n {self.table} will be playing field"

    # def turn(self, played) -> None:
    #     """change who has the turn"""
    #     if played == self.player.name:
    #         self.turn_ = self.player.name
    #     else:
    #         self.turn_ = self.opponent.name
    def format(self) -> str:
        return f"{self.table.get('1') if self.table.get('1') else ' ' }|{self.table.get('2') if self.table.get('2') else ' ' }|{self.table.get('3') if self.table.get('3') else ' ' }\n- - -\n{self.table.get('4') if self.table.get('4') else ' ' }|{self.table.get('5') if self.table.get('5') else ' ' }|{self.table.get('6') if self.table.get('6') else ' ' }\n- - -\n{self.table.get('7') if self.table.get('7') else ' ' }|{self.table.get('8') if self.table.get('8') else ' ' }|{self.table.get('9') if self.table.get('9') else ' ' }\n"

    def first_mover(self) -> bool:
        return True if self.first == self.player.player else False

    def cell(self, ind: str) -> bool:
        """check if cell is already taken"""
        return True if self.table.get(ind) not in Tic_Tac_Toe.xo else False

    def tie(self, window: sg.Window) -> bool:
        """To check if all cells are filled"""

        for cell in self.table.values():
            if cell not in Tic_Tac_Toe.xo:  # if a cell has no value return true
                return True
        window["-POPUP-"].update("Tie")
        window["-RETRY-"].update(visible=True)
        return False

    def win(self, window: sg.Window) -> dict[str, str] | None:
        if (
            self.table.get(str(1)) == self.player
            and self.table.get(str(1 + 1)) == self.player
            and self.table.get(str(1 + 2)) == self.player
            or self.table.get(str(1)) == self.player
            and self.table.get(str(1 + 3)) == self.player
            and self.table.get(str(1 + 6)) == self.player
            or self.table.get(str(1)) == self.player
            and self.table.get(str(1 + 4)) == self.player
            and self.table.get(str(1 + 8)) == self.player
            or self.table.get(str(9)) == self.player
            and self.table.get(str(9 - 1)) == self.player
            and self.table.get(str(9 - 2)) == self.player
            or self.table.get(str(9)) == self.player
            and self.table.get(str(9 - 3)) == self.player
            and self.table.get(str(9 - 6)) == self.player
            or self.table.get(str(5)) == self.player
            and self.table.get(str(5 - 3)) == self.player
            and self.table.get(str(5 + 3)) == self.player
            or self.table.get(str(5)) == self.player
            and self.table.get(str(5 - 1)) == self.player
            and self.table.get(str(5 + 1)) == self.player
            or self.table.get(str(5)) == self.player
            and self.table.get(str(5 - 2)) == self.player
            and self.table.get(str(5 + 2)) == self.player
        ):
            window["-POPUP-"].update("You win")
            window["-RETRY-"].update(visible=True)
            return {"win": self.player.name}

    def lose(self, window: sg.Window) -> dict[str, str] | None:
        if (
            self.table.get(str(1)) == self.opponent
            and self.table.get(str(1 + 1)) == self.opponent
            and self.table.get(str(1 + 2)) == self.opponent
            or self.table.get(str(1)) == self.opponent
            and self.table.get(str(1 + 3)) == self.opponent
            and self.table.get(str(1 + 6)) == self.opponent
            or self.table.get(str(1)) == self.opponent
            and self.table.get(str(1 + 4)) == self.opponent
            and self.table.get(str(1 + 8)) == self.opponent
            or self.table.get(str(9)) == self.opponent
            and self.table.get(str(9 - 1)) == self.opponent
            and self.table.get(str(9 - 2)) == self.opponent
            or self.table.get(str(9)) == self.opponent
            and self.table.get(str(9 - 3)) == self.opponent
            and self.table.get(str(9 - 6)) == self.opponent
            or self.table.get(str(5)) == self.opponent
            and self.table.get(str(5 - 3)) == self.opponent
            and self.table.get(str(5 + 3)) == self.opponent
            or self.table.get(str(5)) == self.opponent
            and self.table.get(str(5 - 1)) == self.opponent
            and self.table.get(str(5 + 1)) == self.opponent
            or self.table.get(str(5)) == self.opponent
            and self.table.get(str(5 - 2)) == self.opponent
            and self.table.get(str(5 + 2)) == self.opponent
        ):
            window["-POPUP-"].update("You lose")
            window["-RETRY-"].update(visible=True)
            return {"win": self.opponent.name}
