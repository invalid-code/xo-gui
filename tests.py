import copy as cp
import unittest

from Tic_Tac_Toe.ai import DecisionTree
from Tic_Tac_Toe.game import TicTacToe


class TestTicTacToeWin(unittest.TestCase):
    def test_win_player(self):
        # * player = X
        game = TicTacToe()
        for cell in range(9):
            # game.table[cell] = TicTacToe.xo[0]
            game.set_cell([(cell, TicTacToe.xo[0])])
            if cell in (2, 5, 8):
                self.assertTrue(game.win())
                game = TicTacToe()

        game = TicTacToe()
        for cell in range(0, 9, 3):
            game.set_cell([(cell, TicTacToe.xo[0])])
            if cell in (6, 7, 8):
                self.assertTrue(game.win())
                game = TicTacToe()

        game = TicTacToe()
        for cell in range(0, 9, 4):
            game.set_cell([(cell, TicTacToe.xo[0])])
            if cell == 8:
                self.assertTrue(game.win())
                game = TicTacToe()

        for cell in range(3, 8, 2):
            game.set_cell([(cell, TicTacToe.xo[0])])
            if cell == 6:
                self.assertTrue(game.win())
                game = TicTacToe()


if __name__ == "__main__":
    unittest.main()
