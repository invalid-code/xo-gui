# pylint: disable=C0114
# pylint: disable=C0115
import unittest
from Tic_Tac_Toe.game import TicTacToe


class TestTicTacToeWin(unittest.TestCase):
    # pylint: disable=C0116
    def __init__(self):
        super().__init__()
        self.game = TicTacToe()

    def test_win_player_horizontal(self):
        for cell in range(9):
            self.game.set_cell([(cell, self.game.player.player)])
            if cell in (2, 5, 8):
                self.assertTrue(self.game.win())
                self.game = TicTacToe()

    def test_win_player_vertical(self):
        for i in range(3):
            for cell in range(i, 9, 3):
                self.game.set_cell([(cell, self.game.player.player)])
                if cell in (6, 7, 8):
                    self.assertTrue(self.game.win())
                    self.game = TicTacToe()

    def test_win_player_diagonal(self):
        self.game = TicTacToe()
        for cell in range(0, 9, 4):
            self.game.set_cell([(cell, self.game.player.player)])
            if cell == 8:
                self.assertTrue(self.game.win())
                self.game = TicTacToe()

        self.game = TicTacToe()
        for cell in range(3, 8, 2):
            self.game.set_cell([(cell, self.game.player.player)])
            if cell == 6:
                self.assertTrue(self.game.win())
                self.game = TicTacToe()


class TestTicTacToeLose(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.game = TicTacToe()

    def test_lose_player_horizontal(self):
        for cell in range(9):
            self.game.set_cell([(cell, self.game.opponent.opponent)])
            if cell in (2, 5, 8):
                self.assertTrue(self.game.lose())
                self.game = TicTacToe()

    def test_lose_player_vertical(self):
        for i in range(3):
            for cell in range(i, 9, 3):
                self.game.set_cell([(cell, self.game.opponent.opponent)])
                if cell in (6, 7, 8):
                    self.assertTrue(self.game.lose())
                    self.game = TicTacToe()

    def test_lose_player_diagonal(self):
        for cell in range(0, 9, 4):
            self.game.set_cell([(cell, self.game.opponent.opponent)])
            if cell == 8:
                self.assertTrue(self.game.lose())
                self.game = TicTacToe()

        for cell in range(3, 8, 2):
            self.game.set_cell([(cell, self.game.opponent.opponent)])
            if cell == 6:
                self.assertTrue(self.game.lose())
                self.game = TicTacToe()


class TestTicTacToeTie(unittest.TestCase):
    def __init__(self) -> None:
        super().__init__()
        self.game = TicTacToe()

    def test_game_tie(self):
        for cell in range(9):
            self.game.set_cell([(cell, self.game.player.player)])
        self.assertTrue(self.game.tie())
        game = TicTacToe()
        for cell in range(9):
            game.set_cell([(cell, game.opponent.opponent)])
        self.assertTrue(game.tie())


if __name__ == "__main__":
    unittest.main()
