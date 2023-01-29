from Tic_Tac_Toe.game import TicTacToe
from Tic_Tac_Toe.players import Player
from Tic_Tac_Toe.ai import minimax
import time


def test():
    # inialization
    game = TicTacToe()
    game.player.player = Player.xo[0]
    game.opponent.opponent = Player.xo[1]
    game.set_cell(
        [
            (0, game.player.player),
            # (1, game.player.player),
            # (6, game.player.player),
            # (2, game.opponent.opponent),
            # (4, game.opponent.opponent),
        ]
    )
    game.turn(game.opponent.name)
    # inialization done

    # test inialization
    print("player: ", game.player.player)
    print("opponent: ", game.opponent.opponent)
    game.game_state()
    print("-----------------------------------")

    # testing ai
    start = time.perf_counter()
    move = minimax(game)
    print(move)
    end = time.perf_counter()
    print(f"Program end: {end - start}")
    # opponent.play()


if __name__ == "__main__":
    test()
