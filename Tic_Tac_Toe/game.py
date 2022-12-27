import random as rd
from dataclasses import dataclass, field

from .players import Player, PlayerA, PlayerB


@dataclass
class TicTacToe:
    """My implemented version of the tic-tac-toe or x's and o's game"""

    # pylint: disable=C0116

    player: PlayerA
    opponent: PlayerB
    ai_score: int = 0
    first: str = rd.choice(Player.names)
    turn_: str = first
    table: list[int | str] = field(
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
        return hash((self.first, self.turn_, tuple(self.table)))

    def __str__(self) -> str:
        return f"player = {self.player}\
                opponent = {self.opponent}\
                first = {self.first}\
                turn = {self.turn_}\
                table = \n{self.get_cell(0, default=' ')}|{self.get_cell(1, default=' ')}|{self.get_cell(2, default=' ')}\n- - -\n{self.get_cell(3, default=' ')}|{self.get_cell(4, default=' ')}|{self.get_cell(5, default=' ')}\n- - -\n{self.get_cell(6, default=' ')}|{self.get_cell(7, default=' ')}|{self.get_cell(8, default=' ')}\n"

    def update_ai_score(self, score) -> None:
        self.ai_score = score

    def game_state(self) -> None:
        print(
            f"\n\
              {self.get_cell(0, default=' ')}|{self.get_cell(1, default=' ')}|{self.get_cell(2, default=' ')}\
              \n- - -\n\
              {self.get_cell(3, default=' ')}|{self.get_cell(4, default=' ')}|{self.get_cell(5, default=' ')}\
              \n- - -\n\
              {self.get_cell(6, default=' ')}|{self.get_cell(7, default=' ')}|{self.get_cell(8, default=' ')}\
              \n"
        )

    def turn(self, name: str | None = None) -> None:
        """change turn of game"""
        if not name:
            self.turn_ = "player" if self.turn_ == "opponent" else "opponent"
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
        if not self.cell(cell_):
            return self.table[cell_]
        else:
            return default

    def set_cell(self, coordinates: list[tuple[int, str]]) -> None:
        for cell_i, cell_ in coordinates:
            self.table[cell_i] = cell_

    def first_mover(self) -> str:
        """
        Returns:
            str: name of the player that moves first
        """
        if self.first == "opponent":
            return "player"
        else:
            return "opponent"

    def tie(self) -> bool:
        for ind, cell in enumerate(self.table):
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
