from back import Tic_Tac_Toe, minimax


def test():
    # inialization
    game = Tic_Tac_Toe()
    game.set_cell(**{"1": "O", "3": "X", "4": "X", "6": "X", "8": "O", "9": "O"})
    game.turn(game.opponent.name)
    # inialization done
    
    # test inialization
    game.format()

    # testing
    minimax(game)

if __name__ == "__main__":
    test()