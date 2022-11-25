import copy as cp
from back import Tic_Tac_Toe, Decision_Tree


def test_win_met():
    # initialize
    game = Tic_Tac_Toe()

    try:
        # test rows
        player_game_cp = cp.deepcopy(game)
        opponent_game_cp = cp.deepcopy(game)
        print("rows-player")
        print("-----------")
        for row in player_game_cp.table.keys():
            for col in row:
                player_game_cp.set_cell(**{col: game.player.player})
                print(player_game_cp.win())
                player_game_cp.format()
            if player_game_cp.win():
                player_game_cp = cp.deepcopy(game)

        print("cols-player")
        print("-----------")

        # test cols
        for col in ("1", "2", "3"):
            for row in range(int(col), int(col)+7, 3):
                player_game_cp.set_cell(**{str(row): player_game_cp.player.player})
                print(player_game_cp.win())
                player_game_cp.format()
            if player_game_cp.win():
                player_game_cp = cp.deepcopy(game)

        print("diag-player-1-9")
        print("-----------")

        # test diag
        col = "1"
        for row in range(int(col), int(col)+10, 4):
            player_game_cp.set_cell(**{str(row): player_game_cp.player.player})
            print(player_game_cp.win())
            player_game_cp.format()

        print("diag-player-3-7")
        print("-----------")

        # test diag
        col = "3"
        for row in range(int(col), int(col)+5, 2):
            player_game_cp.set_cell(**{str(row): player_game_cp.player.player})
            print(player_game_cp.win())
            player_game_cp.format()

        print("rows-opponent")
        print("-------------")

        # test cols
        for col in opponent_game_cp.table.keys():
            for row in col:
                opponent_game_cp.set_cell(**{row: opponent_game_cp.opponent.player})
                print(opponent_game_cp.lose())
                opponent_game_cp.format()
            if opponent_game_cp.lose():
                opponent_game_cp = cp.deepcopy(game)

        print("cols-opponent")
        print("-------------")

        # test cols
        for col in ("1", "2", "3"):
            for row in range(int(col), int(col)+7, 3):
                opponent_game_cp.set_cell(**{str(row): opponent_game_cp.player.player})
                print(opponent_game_cp.win())
                opponent_game_cp.format()
            if opponent_game_cp.win():
                opponent_game_cp = cp.deepcopy(game)
    except Exception as exc:
        print(exc)

def test_find_branch_decision_tree():
    # initialization
    game = Tic_Tac_Toe()
    game.set_cell(**{"1": game.player.player, "2": game.player.player})
    game.turn(game.player.name)
    decision_tree = Decision_Tree(game)
    for branch in range(3, 6):
            game_cp = cp.deepcopy(game)
            game_cp.set_cell(**{str(branch):game_cp.player.player})
            decision_tree.update_decision_tree({branch:game_cp})

    try:
        branch = cp.deepcopy(game)
        branch.set_cell(**{"1": branch.player.player, "2": branch.player.player, "5": branch.player.player})
        found_branch = decision_tree.find_branch(branch)
        print(found_branch)
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    # test_win_met()
    test_find_branch_decision_tree()