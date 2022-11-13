import random as rd
import copy as cp
import PySimpleGUI as sg


class Player:
    def __init__(self, game, player_avatar: str, name: str):
        self.game = game
        self.player = player_avatar
        self.name = name  # to know who is the player and the opponent(ai)

    def __repr__(self) -> str:
        return f"Player(player={self.player}, name={self.name})"

    def __str__(self) -> str:
        return f"player is {self.player}\nplayer is the {self.name}"


class PlayerA(Player):
    def play(self, event: str):
        self.game.turn(self.name)
        ind = event[5]
        if event[1:5] == "CELL":
            self.game.table[ind] = self.player
            return {"cell": event}


class PlayerB(Player):
    def play(self):
        self.game.turn(self.name)
        move = minimax(self.game)


class Tic_Tac_Toe:
    xo = ("X", "O")

    def __init__(self):
        self.player_avatar: str = rd.choice(Tic_Tac_Toe.xo)
        self.player = PlayerA(self, self.player_avatar, "player")
        self.opponent = (
            PlayerB(self, "O", "opponent")
            if self.player_avatar == "X"
            else PlayerB(self, "X", "opponent")
        )
        self.first = rd.choice(Tic_Tac_Toe.xo)
        self.turn_ = (
            self.player.name if self.first == self.player.player else self.opponent.name
        )
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

    def get_cell(self, cell: str) -> str | None:
        return self.table.get(cell)

    def set_cell(self, **kwargs) -> None:
        for key, cell in kwargs.items():
            self.table[key] = cell

    def turn(self, player_name) -> None:
        """change turn of player"""
        self.turn_ = player_name

    def format(self) -> None:
        """log to console the current board state"""
        print()
        print(
            f"{self.table.get('1') if self.table.get('1') else ' ' }|{self.table.get('2') if self.table.get('2') else ' ' }|{self.table.get('3') if self.table.get('3') else ' ' }"
        )
        print("- - -")
        print(
            f"{self.table.get('4') if self.table.get('4') else ' ' }|{self.table.get('5') if self.table.get('5') else ' ' }|{self.table.get('6') if self.table.get('6') else ' ' }"
        )
        print("- - -")
        print(
            f"{self.table.get('7') if self.table.get('7') else ' ' }|{self.table.get('8') if self.table.get('8') else ' ' }|{self.table.get('9') if self.table.get('9') else ' ' }"
        )
        print()

    def first_mover(self) -> str:
        return (
            self.player.name if self.first == self.player.player else self.opponent.name
        )

    def cell(self, ind: str) -> bool:
        """check if cell is already taken"""
        return self.table.get(ind) not in Tic_Tac_Toe.xo

    def tie(self) -> bool:
        """To check if all cells are filled"""
        for cell in self.table.values():
            if cell not in Tic_Tac_Toe.xo:  # if a cell is empty return false
                return False
        return True

    def win(self) -> bool:
        return (
            (
                self.get_cell(str(1)) == self.player.player
                and self.get_cell(str(1 + 1)) == self.player.player
                and self.get_cell(str(1 + 2)) == self.player.player
            )
            or (
                self.get_cell(str(1)) == self.player.player
                and self.get_cell(str(1 + 3)) == self.player.player
                and self.get_cell(str(1 + 6)) == self.player.player
            )
            or (
                self.get_cell(str(1)) == self.player.player
                and self.get_cell(str(1 + 4)) == self.player.player
                and self.get_cell(str(1 + 8)) == self.player.player
            )
            or (
                self.get_cell(str(9)) == self.player
                and self.get_cell(str(9 - 1)) == self.player.player
                and self.get_cell(str(9 - 2)) == self.player.player
            )
            or (
                self.get_cell(str(9)) == self.player.player
                and self.get_cell(str(9 - 3)) == self.player.player
                and self.get_cell(str(9 - 6)) == self.player.player
            )
            or (
                self.get_cell(str(5)) == self.player.player
                and self.get_cell(str(5 - 3)) == self.player.player
                and self.get_cell(str(5 + 3)) == self.player.player
            )
            or (
                self.get_cell(str(5)) == self.player.player
                and self.get_cell(str(5 - 1)) == self.player.player
                and self.get_cell(str(5 + 1)) == self.player.player
            )
            or (
                self.get_cell(str(5)) == self.player.player
                and self.get_cell(str(5 - 2)) == self.player.player
                and self.get_cell(str(5 + 2)) == self.player.player
            )
        )

    def lose(self) -> bool:
        return (
            (
                self.table.get(str(1)) == self.opponent.player
                and self.get_cell(str(1 + 1)) == self.opponent.player
                and self.get_cell(str(1 + 2)) == self.opponent.player
            )
            or (
                self.get_cell(str(1)) == self.opponent.player
                and self.get_cell(str(1 + 3)) == self.opponent.player
                and self.get_cell(str(1 + 6)) == self.opponent.player
            )
            or (
                self.get_cell(str(1)) == self.opponent.player
                and self.get_cell(str(1 + 4)) == self.opponent.player
                and self.get_cell(str(1 + 8)) == self.opponent.player
            )
            or (
                self.get_cell(str(9)) == self.opponent.player
                and self.get_cell(str(9 - 1)) == self.opponent.player
                and self.get_cell(str(9 - 2)) == self.opponent.player
            )
            or (
                self.get_cell(str(9)) == self.opponent.player
                and self.get_cell(str(9 - 3)) == self.opponent.player
                and self.get_cell(str(9 - 6)) == self.opponent.player
            )
            or (
                self.get_cell(str(5)) == self.opponent.player
                and self.get_cell(str(5 - 3)) == self.opponent.player
                and self.get_cell(str(5 + 3)) == self.opponent.player
            )
            or (
                self.get_cell(str(5)) == self.opponent.player
                and self.get_cell(str(5 - 1)) == self.opponent.player
                and self.get_cell(str(5 + 1)) == self.opponent.player
            )
            or (
                self.get_cell(str(5)) == self.opponent.player
                and self.get_cell(str(5 - 2)) == self.opponent.player
                and self.get_cell(str(5 + 2)) == self.opponent.player
            )
        )


def minimax(game: Tic_Tac_Toe, depth=0):
    if game.win():
        print(-1, "you win")
    if game.lose():
        print(1, "you lose")
    if game.tie():
        print(0, "tie")

    opponent_row:list[Tic_Tac_Toe] = []
    player_row:list[Tic_Tac_Toe] = []
    for key in game.table.keys():
        game_copy = cp.deepcopy(game)
        if game_copy.cell(key):
            if game_copy.turn_ == game_copy.opponent.name:
                game_copy.set_cell(**{key: game_copy.opponent.player})
                game_copy.turn(game_copy.player.player)
                game_copy.format()
                opponent_row.append(game_copy)
            else:
                game_copy.set_cell(**{key: game_copy.player.player})
                game_copy.turn(game_copy.opponent.player)
                game_copy.format()
                player_row.append(game_copy)
    if game.turn_ == game.opponent.name:
        for branch in opponent_row:
            minimax(branch)
    else:
        for branch in player_row:
            minimax(branch)
