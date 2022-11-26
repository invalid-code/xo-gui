from back import minimax, TicTacToe


def test():
    # inialization
    game = TicTacToe()
    game.set_cell(**{"1": "O", "3": "X", "4": "X", "6": "X", "8": "O", "9": "O"})
    game.turn(game.opponent.name)
    # inialization done

    # test inialization
    print("player: ", game.player.player)
    print("opponent: ", game.opponent.player)
    game.format()
    print("-----------------------------------")

    # testing
    minimax(game)


if __name__ == "__main__":
    test()
