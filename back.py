import random as rd
import copy as cp

# import PySimpleGUI as sg
from typing import ClassVar
from dataclasses import dataclass, field


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
    def play(self, event: str) -> dict[str, str] | None:
        self.game.turn(self.name)
        ind = event[5]
        if event[1:5] == "CELL":
            self.game.table[ind] = self.player
            return {"cell": event}


class PlayerB(Player):
    def play(self) -> None:
        self.game.turn(self.name)
        move = minimax(self.game)


@dataclass
class TicTacToe:
    xo: ClassVar[tuple] = ("X", "O")
    player_avatar: str = rd.choice(xo)
    first: str = rd.choice(xo)
    table: dict[str, str] = field(
        default_factory=lambda: {
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
    )

    def __post_init__(self):
        self.player = PlayerA(self, self.player_avatar, "player")
        self.opponent = (
            PlayerB(self, "O", "opponent")
            if self.player_avatar == "X"
            else PlayerB(self, "X", "opponent")
        )
        self.turn_ = (
            self.player.name if self.first == self.player.player else self.opponent.name
        )

    def __str__(self) -> str:
        return f"""{self.table.get('1') if self.table.get('1') else ' ' }|{self.table.get('2') if self.table.get('2') else ' ' }|{self.table.get('3') if self.table.get('3') else ' ' }
- - -
{self.table.get('4') if self.table.get('4') else ' ' }|{self.table.get('5') if self.table.get('5') else ' ' }|{self.table.get('6') if self.table.get('6') else ' ' }
- - -
{self.table.get('7') if self.table.get('7') else ' ' }|{self.table.get('8') if self.table.get('8') else ' ' }|{self.table.get('9') if self.table.get('9') else ' ' }"""

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
        return self.table.get(ind) not in TicTacToe.xo

    def tie(self) -> bool:
        """To check if all cells are filled"""
        for cell in self.table.values():
            if cell not in TicTacToe.xo:  # if a cell is empty return false
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


class DecisionTree:
    def __init__(self, root_node: TicTacToe) -> None:
        self.decision_tree: dict[int, TicTacToe | dict[int, TicTacToe]] = {}
        self.tree_row = 0
        if len(self.decision_tree) == 0:
            self.update_decision_tree(root_node)

    def __repr__(self) -> str:
        return f"DecisionTree(decision_tree='{self.decision_tree}', tree_row='{self.tree_row}')"

    def update_decision_tree(self, branches: dict[int, TicTacToe] | TicTacToe) -> None:
        if isinstance(branches, dict):
            self.add_tree_row()
        self.decision_tree.update({self.tree_row: branches})

    def add_tree_row(self):
        self.tree_row += 1

    def update_branch_score(self, coordinates: tuple[int, int], score: int) -> None:
        """mutate branch score

        Args:
            coordinates (tuple[int, int]): to find where branch is located
            score (int): score to give the branch
        """
        tree_row = self.decision_tree.get(coordinates[0])
        branch = tree_row.get(coordinates[1])
        node = {"game": branch, "score": score}
        tree_row.update({coordinates[1]: node})

    def find_branch(
        self,
        branch: TicTacToe,
    ) -> tuple[int, int] | None:
        """find a branch in the decision tree

        Args:
            branch (TicTacToe): branch to find
            coordinates (tuple[int,int]): coodinates of a branch

        Returns:
            tuple[int, int] | None: coordinates of the branch if it exist's
        """
        for (
            tree_row_no,
            decision_tree_row,
        ) in (
            self.decision_tree.items()
        ):  # for name, age in dictionary.iteritems():  (for Python 2.x)
            #     print(branch_no, decision_tree_row)
            if isinstance(decision_tree_row, TicTacToe):
                continue
            for (
                decision_tree_branch_no,
                decision_tree_branch,
            ) in decision_tree_row.items():
                if decision_tree_branch.__eq__(branch):
                    return (tree_row_no, decision_tree_branch_no)


def best_move(decision_tree: DecisionTree):
    """_summary_

    Args:
        decision_tree (DecisionTree): _description_
    """
    pass


def minimax(
    game: TicTacToe,
    depth=0,
    decision_tree: DecisionTree | None = None,
    branch_no: int = 0,
):
    # TODO: go backwards to the decision tree and give score

    if decision_tree is None:
        decision_tree = DecisionTree(game)

    if game.win():
        return 0
    elif game.lose():
        return 1
    elif game.tie():
        return 0

    opponent_row: dict[int, TicTacToe] = {}
    player_row: dict[int, TicTacToe] = {}
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
            if score is not None:
                find_branch_decision_tree = decision_tree.find_branch(branch)
                decision_tree.update_branch_score(
                    find_branch_decision_tree, score
                )  # terminal node
                for parent_tree_row_no in range(
                    find_branch_decision_tree[0] - 1, 0, -1
                ):
                    parent_branch = decision_tree.decision_tree.get(
                        parent_tree_row_no
                    ).get(find_branch_decision_tree[1])
                    if parent_branch.turn_ == game.opponent.name:
                        if score is 1:
                            decision_tree.update_branch_score(
                                (parent_tree_row_no, find_branch_decision_tree[1]),
                                score,
                            )
                    else:
                        if score is -1:
                            decision_tree.update_branch_score(
                                (parent_tree_row_no, find_branch_decision_tree[1]),
                                score,
                            )
    else:
        decision_tree.update_decision_tree(player_row)
        for branch_no, branch in player_row.items():
            score = minimax(branch, decision_tree=decision_tree, branch_no=branch_no)
            if score is not None:
                find_branch_decision_tree = decision_tree.find_branch(branch)
                decision_tree.update_branch_score(
                    find_branch_decision_tree, score
                )  # terminal node
                for parent_tree_row_no in range(
                    find_branch_decision_tree[0] - 1, 0, -1
                ):
                    # decision_tree.get(parent_tree_row_no).get(find_branch_decision_tree[1])
                    # decision_tree.update_branch_score(
                    #     (parent_tree_row_no, find_branch_decision_tree[1]), score
                    # )
                    parent_branch = decision_tree.decision_tree.get(
                        parent_tree_row_no
                    ).get(find_branch_decision_tree[1])
                    if parent_branch.turn_ == game.opponent.name:
                        if score is 1:
                            decision_tree.update_branch_score(
                                (parent_tree_row_no, find_branch_decision_tree[1]),
                                score,
                            )
                    else:
                        if score is -1:
                            decision_tree.update_branch_score(
                                (parent_tree_row_no, find_branch_decision_tree[1]),
                                score,
                            )
