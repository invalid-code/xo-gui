import copy as cp
import unittest
from back import TicTacToe, DecisionTree


class TestTicTacToeWin(unittest.TestCase):
    # def test_win(self):
    #     game = TicTacToe()

    #     # test rows
    #     player_game_cp = cp.deepcopy(game)
    #     for row in player_game_cp.table.keys():
    #         player_game_cp.set_cell(**{col: player_game_cp.player.player})
    #         self.assertTrue(player_game_cp.win())
    #         if player_game_cp.win():
    #             player_game_cp = cp.deepcopy(game)

    #     # test cols
    #     for col in ("1", "2", "3"):
    #         for row in range(int(col), int(col) + 7, 3):
    #             player_game_cp.set_cell(**{str(row): player_game_cp.player.player})
    #         self.assertTrue(player_game_cp.win())
    #         if player_game_cp.win():
    #             player_game_cp = cp.deepcopy(game)

    #     # test diag-1-9
    #     col = "1"
    #     for row in range(int(col), int(col) + 10, 4):
    #         player_game_cp.set_cell(**{str(row): player_game_cp.player.player})
    #     self.assertTrue(player_game_cp.win())

    #     # test diag-3-7
    #     col = "3"
    #     for row in range(int(col), int(col) + 5, 2):
    #         player_game_cp.set_cell(**{str(row): player_game_cp.player.player})
    #     self.assertTrue(player_game_cp.win())

    # def test_lose(self):
    #     game = TicTacToe()
    #     opponent_game_cp = cp.deepcopy(game)

    #     # test rows
    #     for col in opponent_game_cp.table.keys():
    #         for row in col:
    #             opponent_game_cp.set_cell(**{row: opponent_game_cp.opponent.player})
    #         self.assertTrue(opponent_game_cp.lose())
    #         if opponent_game_cp.lose():
    #             opponent_game_cp = cp.deepcopy(game)

    #     # test cols
    #     for col in ("1", "2", "3"):
    #         for row in range(int(col), int(col) + 7, 3):
    #             opponent_game_cp.set_cell(**{str(row): opponent_game_cp.player.player})
    #         self.assertTrue(opponent_game_cp.lose())
    #         if opponent_game_cp.win():
    #             opponent_game_cp = cp.deepcopy(game)

    #     # test diag-1-9
    #     col = "1"
    #     for row in range(int(col), int(col) + 10, 4):
    #         opponent_game_cp.set_cell(**{str(row): opponent_game_cp.player.player})
    #     self.assertTrue(opponent_game_cp.lose())

    #     # test diag-3-7
    #     col = "3"
    #     for row in range(int(col), int(col) + 5, 2):
    #         opponent_game_cp.set_cell(**{str(row): opponent_game_cp.player.player})
    #     self.assertTrue(opponent_game_cp.win())
    pass


class TestDecisionTree(unittest.TestCase):
    def test_find_branch_decision_tree(self):
        game = TicTacToe()
        tree_row: dict[str, TicTacToe] = {}
        branch_no = 0
        game.set_cell(**{"1": game.player.player, "2": game.player.player})
        game.turn(game.player.name)
        decision_tree = DecisionTree(game)

        for branch in range(3, 6):
            game_cp = cp.deepcopy(game)
            game_cp.set_cell(**{str(branch): game_cp.player.player})
            branch_no += 1
            tree_row.update({branch_no: game_cp})
        decision_tree.update_decision_tree(tree_row)
        branch = cp.deepcopy(game)
        branch.set_cell(
            **{
                "1": branch.player.player,
                "2": branch.player.player,
                "5": branch.player.player,
            }
        )
        found_branch = decision_tree.find_branch(branch)
        self.assertEqual((1, 3), found_branch)
    
    def test_update_branch_score(self):
        game = TicTacToe()
        tree_row: dict[str, TicTacToe] = {}
        branch_no = 0
        game.set_cell(**{"1": game.player.player, "2": game.player.player})
        game.turn(game.player.name)
        decision_tree = DecisionTree(game)

        for branch in range(3, 6):
            game_cp = cp.deepcopy(game)
            game_cp.set_cell(**{str(branch): game_cp.player.player})
            branch_no += 1
            tree_row.update({branch_no: game_cp})
        decision_tree.update_decision_tree(tree_row)
        branch = cp.deepcopy(game)
        branch.set_cell(
            **{
                "1": branch.player.player,
                "2": branch.player.player,
                "5": branch.player.player,
            }
        )
        found_branch = decision_tree.find_branch(branch)
        decision_tree.update_branch_score(found_branch, 0)
        self.assertEqual({"game": branch, "score": 0}, decision_tree.decision_tree.get(found_branch[0]).get(found_branch[1]))
    

if __name__ == "__main__":
    unittest.main()
