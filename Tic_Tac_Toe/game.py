"""game module"""
import random as rd
from dataclasses import dataclass, field

from .players import Opponent, Player


@dataclass
class TicTacToe:
    """My implemented version of the tic-tac-toe or x's and o's game"""

    # pylint: disable=C0116

    player: Player = Player()
    opponent: Opponent = Opponent(player)
    ai_score: int = 0
    first: str = rd.choice((Player.name, Opponent.name))
    turn_: str = first
    table: list[int] = field(
        default_factory=lambda: [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
        ]
    )

    def __hash__(self) -> int:
        return hash(
            (
                self.player,
                self.opponent,
                self.ai_score,
                self.first,
                self.turn_,
                tuple(self.table),
            )
        )

    def __str__(self) -> str:
        return f"player: {self.player}\nopponent: {self.opponent}\nai score: {self.ai_score}\nfirst: {self.first}\nturn: {self.turn_}\ntable: \n{self.get_cell(0, default=' ')}|{self.get_cell(1, default=' ')}|{self.get_cell(2, default=' ')}\n- - -\n{self.get_cell(3, default=' ')}|{self.get_cell(4, default=' ')}|{self.get_cell(5, default=' ')}\n- - -\n{self.get_cell(6, default=' ')}|{self.get_cell(7, default=' ')}|{self.get_cell(8, default=' ')}\n".title()

    def update_ai_score(self, score) -> None:
        self.ai_score = score

    def game_state(self) -> None:
        print(
            f"\n{self.get_cell(0, default=' ')}|{self.get_cell(1, default=' ')}|{self.get_cell(2, default=' ')}\n- - -\n{self.get_cell(3, default=' ')}|{self.get_cell(4, default=' ')}|{self.get_cell(5, default=' ')}\n- - -\n{self.get_cell(6, default=' ')}|{self.get_cell(7, default=' ')}|{self.get_cell(8, default=' ')}\n"
        )

    def turn(self, name: str | None = None) -> None:
        """change turn of game"""
        if not name:
            self.turn_ = Player.name if self.turn_ == Opponent.name else Opponent.name
            return
        self.turn_ = name

    def remaining_cells(self) -> list[int]:
        """get indexes of empty cells

        Returns:
            list[int]: list of empty cell indexes
        """
        return [cell_i for cell_i, cell_ in enumerate(self.table) if self.cell(cell_i)]

    def cell(self, ind: int) -> bool:
        """check if cell is available

        Args:
            ind (int): cell to check

        Returns:
            bool: returns True if cell is a empty(int) False otherwise
        """
        return isinstance(self.table[ind], int)

    def get_cell(self, cell_: int, default: str = " ") -> str:
        """
        Args:
            cell (int): cell coordinates

        Returns:
            str : value of table cell
        """
        return self.table[cell_] if not self.cell(cell_) else default

    def set_cell(self, coordinates: list[tuple[int, str]]) -> None:
        for cell_i, cell_ in coordinates:
            self.table[cell_i] = cell_

    def first_mover(self) -> str:
        """
        Returns:
            str: name of the player that moves first
        """
        return Player.name if self.first == "opponent" else Opponent.name

    def tie(self) -> bool:
        for ind, _ in enumerate(self.table):
            if self.cell(ind):
                # if a cell is empty return false
                return False
        return True

    def win(self) -> bool:
        return (
            (
                self.get_cell(0) == self.player.player
                and self.get_cell(1) == self.player.player
                and self.get_cell(2) == self.player.player
            )
            or (
                self.get_cell(3) == self.player.player
                and self.get_cell(4) == self.player.player
                and self.get_cell(5) == self.player.player
            )
            or (
                self.get_cell(6) == self.player.player
                and self.get_cell(7) == self.player.player
                and self.get_cell(8) == self.player.player
            )
            or (
                self.get_cell(0) == self.player.player
                and self.get_cell(3) == self.player.player
                and self.get_cell(6) == self.player.player
            )
            or (
                self.get_cell(1) == self.player.player
                and self.get_cell(4) == self.player.player
                and self.get_cell(7) == self.player.player
            )
            or (
                self.get_cell(2) == self.player.player
                and self.get_cell(5) == self.player.player
                and self.get_cell(8) == self.player.player
            )
            or (
                self.get_cell(0) == self.player.player
                and self.get_cell(4) == self.player.player
                and self.get_cell(8) == self.player.player
            )
            or (
                self.get_cell(2) == self.player.player
                and self.get_cell(4) == self.player.player
                and self.get_cell(6) == self.player.player
            )
        )

    def lose(self) -> bool:
        return (
            (
                self.get_cell(0) == self.opponent.opponent
                and self.get_cell(1) == self.opponent.opponent
                and self.get_cell(2) == self.opponent.opponent
            )
            or (
                self.get_cell(3) == self.opponent.opponent
                and self.get_cell(4) == self.opponent.opponent
                and self.get_cell(5) == self.opponent.opponent
            )
            or (
                self.get_cell(6) == self.opponent.opponent
                and self.get_cell(7) == self.opponent.opponent
                and self.get_cell(8) == self.opponent.opponent
            )
            or (
                self.get_cell(0) == self.opponent.opponent
                and self.get_cell(3) == self.opponent.opponent
                and self.get_cell(6) == self.opponent.opponent
            )
            or (
                self.get_cell(1) == self.opponent.opponent
                and self.get_cell(4) == self.opponent.opponent
                and self.get_cell(7) == self.opponent.opponent
            )
            or (
                self.get_cell(2) == self.opponent.opponent
                and self.get_cell(5) == self.opponent.opponent
                and self.get_cell(8) == self.opponent.opponent
            )
            or (
                self.get_cell(0) == self.opponent.opponent
                and self.get_cell(4) == self.opponent.opponent
                and self.get_cell(8) == self.opponent.opponent
            )
            or (
                self.get_cell(2) == self.opponent.opponent
                and self.get_cell(4) == self.opponent.opponent
                and self.get_cell(6) == self.opponent.opponent
            )
        )
