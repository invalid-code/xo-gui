import random as rd
from dataclasses import dataclass, field
from typing import ClassVar, Literal

from Tic_Tac_Toe.players import PlayerA, PlayerB


@dataclass
class TicTacToe:
    xo: ClassVar[tuple] = ("X", "O")
    player: PlayerA = field(init=False)
    opponent: PlayerB = field(init=False)
    turn_: str = field(init=False)
    player_avatar: Literal["X", "O"] = rd.choice(xo)
    first: Literal["X", "O"] = rd.choice(xo)
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

    def __post_init__(self):
        self.player = PlayerA(self, self.player_avatar, "player")

        if self.player_avatar == "X":
            self.opponent = PlayerB(self, "O", "opponent")
        else:
            self.opponent = PlayerB(self, "X", "opponent")

        if self.first == self.player.player:
            self.turn_ = self.player.name
        else:
            self.turn_ = self.opponent.name

    def __str__(self) -> str:
        return f"{self.get_cell(0, default=' ')}|{self.get_cell(1, default=' ')}|{self.get_cell(2, default=' ')}\n- - -\n{self.get_cell(3, default=' ')}|{self.get_cell(4, default=' ')}|{self.get_cell(5, default=' ')}\n- - -\n{self.get_cell(6, default=' ')}|{self.get_cell(7, default=' ')}|{self.get_cell(8, default=' ')}"

    def cell(self, ind: int) -> bool:
        """check if cell is available

        Args:
            ind (int): cell to check

        Returns:
            bool: returns True if cell is a empty(int) False otherwise
        """
        return isinstance(self.table[ind], int)

    def get_cell(self, cell_: int, default: str | None = None) -> str:
        """get current cell value

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
        """sets the cell value of game"""
        for cell_ in coordinates:
            self.table[cell_[0]] = cell_[1]

    def turn(self) -> None:
        """change turn of game"""
        if self.turn_ == self.player.name:
            self.turn_ = self.opponent.name
        else:
            self.turn_ = self.player.name

    def format(self) -> None:
        """log to console the current board state"""
        print()
        print(self)
        print()

    def first_mover(self) -> str:
        """return the name of the first player to move

        Returns:
            str: name of the player that moves first
        """
        if self.first == self.player.player:
            return self.player.name
        else:
            return self.opponent.name

    def tie(self) -> bool:
        """To check if all cells are filled"""
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
                self.get_cell(0) == self.opponent.player
                and self.get_cell(1) == self.opponent.player
                and self.get_cell(2) == self.opponent.player
            )
            or (
                self.get_cell(3) == self.opponent.player
                and self.get_cell(4) == self.opponent.player
                and self.get_cell(5) == self.opponent.player
            )
            or (
                self.get_cell(6) == self.opponent.player
                and self.get_cell(7) == self.opponent.player
                and self.get_cell(8) == self.opponent.player
            )
            or (
                self.get_cell(1) == self.opponent.player
                and self.get_cell(3) == self.opponent.player
                and self.get_cell(6) == self.opponent.player
            )
            or (
                self.get_cell(1) == self.opponent.player
                and self.get_cell(4) == self.opponent.player
                and self.get_cell(7) == self.opponent.player
            )
            or (
                self.get_cell(2) == self.opponent.player
                and self.get_cell(5) == self.opponent.player
                and self.get_cell(8) == self.opponent.player
            )
            or (
                self.get_cell(0) == self.opponent.player
                and self.get_cell(4) == self.opponent.player
                and self.get_cell(8) == self.opponent.player
            )
            or (
                self.get_cell(2) == self.opponent.player
                and self.get_cell(4) == self.opponent.player
                and self.get_cell(6) == self.opponent.player
            )
        )
