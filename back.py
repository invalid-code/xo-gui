import random as rd
import copy as cp

# import PySimpleGUI as sg
from typing import ClassVar
from dataclasses import dataclass


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


@dataclass
class Tic_Tac_Toe:
    xo: ClassVar[tuple] = ("X", "O")
    player_avatar: str = rd.choice(xo)
    player: PlayerA = PlayerA(self, player_avatar, "player")
    opponent: PlayerB = (
        PlayerB(self, "O", "opponent")
        if player_avatar == "X"
        else PlayerB(self, "X", "opponent")
    )
    first: str = rd.choice(xo)
    turn_: str = player.name if first == player.player else opponent.name
    table: dict[str, str] = {
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
                self.get_cell(str(9)) == self.player.player
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
                self.get_cell(str(1)) == self.opponent.player
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


class Decision_Tree:
    def __init__(self, root_node: Tic_Tac_Toe) -> None:
        self.decision_tree: dict[int, Tic_Tac_Toe | dict[int, Tic_Tac_Toe]] = {}
        self.tree_row = 0
        if len(self.decision_tree) == 0:
            self.update_decision_tree(root_node)

    def update_decision_tree(self, branches: dict[int, Tic_Tac_Toe] | Tic_Tac_Toe):
        if isinstance(branches, dict):
            self.add_tree_row()
        self.decision_tree.update({self.tree_row: branches})

    def add_tree_row(self):
        self.tree_row += 1

    def update_branch_score(self):
        return

    def find_branch(self, branch: Tic_Tac_Toe):
        # print(self.decision_tree)
        for (
            tree_row_no,
            decision_tree_row,
        ) in (
            self.decision_tree.items()
        ):  # for name, age in dictionary.iteritems():  (for Python 2.x)
            #     print(branch_no, decision_tree_row)
            if isinstance(decision_tree_row, Tic_Tac_Toe):
                continue
            for (
                decision_tree_branch_no,
                decision_tree_branch,
            ) in decision_tree_row.items():
                print(decision_tree_branch.__eq__(branch))
                if decision_tree_branch.__eq__(branch):
                    return (tree_row_no, decision_tree_branch_no)


def minimax(
    game: Tic_Tac_Toe,
    depth=0,
    decision_tree: Decision_Tree | None = None,
    branch_no: int = 0,
):
    # TODO if we score change decision tree
    if decision_tree is None:
        decision_tree = Decision_Tree(game)

    if game.win():
        return 1
    elif game.lose():
        return -1
    elif game.tie():
        return 0

    opponent_row: dict[int, Tic_Tac_Toe] = {}
    player_row: dict[int, Tic_Tac_Toe] = {}
    branch_no_ = 0

    for key in game.table.keys():
        if game.cell(key):
            game_copy = cp.deepcopy(game)
            if game_copy.turn_ == game_copy.opponent.name:
                game_copy.set_cell(**{key: game_copy.opponent.player})
                game_copy.turn(game_copy.player.name)
                if branch_no == 0:
                    branch_no_ += 1
                    opponent_row.update({branch_no_: game_copy})
                else:
                    opponent_row.update({branch_no: game_copy})
            else:
                game_copy.set_cell(**{key: game_copy.player.player})
                game_copy.turn(game_copy.opponent.name)
                if branch_no == 0:
                    branch_no_ += 1
                    player_row.update({branch_no_: game_copy})
                else:
                    player_row.update({branch_no: game_copy})
            # game_copy.format()

    if game.turn_ == game.opponent.name:
        decision_tree.update_decision_tree(opponent_row)
        for branch_no, branch in opponent_row.items():
            score = minimax(branch, decision_tree=decision_tree, branch_no=branch_no)
            if score:
                find_branch_decision = decision_tree.find_branch(branch)
                # print(find_branch_decision)
                # print(decision_tree.decision_tree.get(find_branch_decision[0]))

    else:
        decision_tree.update_decision_tree(player_row)
        for branch_no, branch in player_row.items():
            score = minimax(branch, decision_tree=decision_tree, branch_no=branch_no)
            if score:
                find_branch_decision = decision_tree.find_branch(branch)
                # print(find_branch_decision)
                # print(decision_tree.decision_tree.get(find_branch_decision[0]))
