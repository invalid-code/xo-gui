from Tic_Tac_Toe.game import TicTacToe


def test():
    # inialization
    game = TicTacToe()
    game.opponent.player = TicTacToe.xo[0]
    game.player.player = TicTacToe.xo[1]
    game.set_cell(
        [
            (0, TicTacToe.xo[0]),
            (2, TicTacToe.xo[1]),
            (3, TicTacToe.xo[0]),
            (5, TicTacToe.xo[0]),
            (6, TicTacToe.xo[1]),
            (7, TicTacToe.xo[1]),
        ]
    )
    game.turn_ = game.opponent.name
    # game.turn(game.opponent.name)
    # inialization done

    # test inialization
    print("player: ", game.player.player)
    print("opponent: ", game.opponent.player)
    game.format()
    print("-----------------------------------")

    # testing ai
    game.opponent.play()


if __name__ == "__main__":
    test()
