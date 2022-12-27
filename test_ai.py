from Tic_Tac_Toe.game import TicTacToe
from Tic_Tac_Toe.players import PlayerA, PlayerB, Player
from Tic_Tac_Toe.ai import minimax


def test():
    # inialization
    game = TicTacToe(player=PlayerA(), opponent=PlayerB())
    game.player.player = Player.xo[0]
    game.opponent.opponent = Player.xo[1]
    game.set_cell(
        [
            (0, game.player.player),
            (2, game.opponent.opponent),
            (3, game.player.player),
            (5, game.player.player),
            (6, game.opponent.opponent),
            (7, game.opponent.opponent),
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
    minimax(game)
    # opponent.play()


if __name__ == "__main__":
    test()
