# pylint: disable=C0114
# pylint: disable=C0115
import unittest

from Tic_Tac_Toe.game import TicTacToe
from Tic_Tac_Toe.players import PlayerA, PlayerB


class TestTicTacToeWin(unittest.TestCase):
    def test_win_player_horizontal(self):
        player = PlayerA()
        opponent = PlayerB()
        game = TicTacToe(player=player, opponent=opponent)
        for cell in range(9):
            game.set_cell([(cell, game.player.player)])
            if cell in (2, 5, 8):
                self.assertTrue(game.win())
                game = TicTacToe(player=player, opponent=opponent)

    def test_win_player_vertical(self):
        player = PlayerA()
        opponent = PlayerB()
        game = TicTacToe(player=player, opponent=opponent)
        for i in range(3):
            for cell in range(i, 9, 3):
                game.set_cell([(cell, game.player.player)])
                if cell in (6, 7, 8):
                    self.assertTrue(game.win())
                    game = TicTacToe(player=player, opponent=opponent)

    def test_win_player_diagonal(self):
        player = PlayerA()
        opponent = PlayerB()
        game = TicTacToe(player=player, opponent=opponent)
        for cell in range(0, 9, 4):
            game.set_cell([(cell, game.player.player)])
            if cell == 8:
                self.assertTrue(game.win())
                game = TicTacToe(player=player, opponent=opponent)

        game = TicTacToe(player=player, opponent=opponent)
        for cell in range(3, 8, 2):
            game.set_cell([(cell, game.player.player)])
            if cell == 6:
                self.assertEqual(game.win())
                game = TicTacToe(player=player, opponent=opponent)


class TestTicTacToeLose(unittest.TestCase):
    def test_lose_player_horizontal(self):
        player = PlayerA()
        opponent = PlayerB()
        game = TicTacToe(player=player, opponent=opponent)
        for cell in range(9):
            game.set_cell([(cell, game.opponent.opponent)])
            if cell in (2, 5, 8):
                self.assertTrue(game.lose())
                game = TicTacToe(player=player, opponent=opponent)

    def test_lose_player_vertical(self):
        player = PlayerA()
        opponent = PlayerB()
        game = TicTacToe(player=player, opponent=opponent)
        for i in range(3):
            for cell in range(i, 9, 3):
                game.set_cell([(cell, game.opponent.opponent)])
                if cell in (6, 7, 8):
                    self.assertTrue(game.lose())
                    game = TicTacToe(player=player, opponent=opponent)

    def test_lose_player_diagonal(self):
        player = PlayerA()
        opponent = PlayerB()
        game = TicTacToe(player=player, opponent=opponent)
        for cell in range(0, 9, 4):
            game.set_cell([(cell, game.opponent.opponent)])
            if cell == 8:
                self.assertTrue(game.lose())
                game = TicTacToe(player=player, opponent=opponent)

        for cell in range(3, 8, 2):
            game.set_cell([(cell, game.opponent.opponent)])
            if cell == 6:
                self.assertEqual(game.lose())
                game = TicTacToe(player=player, opponent=opponent)


class TestTicTacToeTie(unittest.TestCase):
    def test_tie(self):
        player = PlayerA()
        opponent = PlayerB()
        game = TicTacToe(player=player, opponent=opponent)
        for cell in range(9):
            game.set_cell([(cell, game.player.player)])
        self.assertTrue(game.tie())
        game = TicTacToe(player=player, opponent=opponent)
        for cell in range(9):
            game.set_cell([(cell, game.opponent.opponent)])
        self.assertTrue(game.tie())


if __name__ == "__main__":
    unittest.main()
