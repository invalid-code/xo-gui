#!/usr/bin/env python

import random as rd

import PySimpleGUI as sg

sg.theme("dark grey")


class Player:
    def __init__(self, player_avatar: str, is_player_opponent: str):
        self.player = player_avatar
        self.is_player_opponent = is_player_opponent

    def __repr__(self):
        return f"Player(player={self.player}, is_player_opponent={self.is_player_opponent})"

    def __str__(self):
        return f"player is {self.player}\nplayer is the {self.is_player_opponent}"


class PlayerA(Player):
    def play(self, game, window: sg.Window, event: str):
        ind = event[5]
        if event[1:5] == "CELL":
            game.table[ind] = self.player
            window[f"-CELL{ind}-"].update(self.player)


class PlayerB(Player):
    def play(self, game, window: sg.Window):
        # temporary
        for key, cell in game.table.items():
            if not cell:
                game.table[key] = self.player
                print(game.table)
                window[f"-CELL{key}-"].update(self.player)
                window.refresh()
                break


class Game:
    xo = ("X", "O")

    def __init__(self):
        self.player_avatar = rd.choice(Game.xo)
        self.player = PlayerA(self.player_avatar, "player")
        if self.player_avatar == "X":
            self.opponent = PlayerB("O", "opponent")
        else:
            self.opponent = PlayerB("X", "opponent")
        self.first = rd.choice(Game.xo)
        self.table = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": "",
            "9": "",
        }

    def __repr__(self):
        return f"Game(player_avatar={self.player_avatar}, player={self.player.__repr__()}, opponent={self.opponent.__repr__()}, first={self.first}, table={self.table})"

    def __str__(self):
        return f"the player's avatar will be {self.player_avatar}\nplayer will be {self.player}\nopponent will be {self.opponent}\n {self.player if self.first else self.opponent}\n {self.table} will be playing field"

    def get_cell_value(self, ind: str):
        return self.table.get(ind)

    def is_player_first(self):
        if self.first == self.player.player:
            return True
        return False

    def finished_game(self, window: sg.Window):
        """To check if all cells are filled"""

        for cell in self.table.values():

            if cell not in Game.xo:  # if a cell has no value return true
                return True

        window["-POPUP-"].update("Tie")
        window["-RETRY-"].update(visible=True)
        return False

    def check_cell(self, ind: str):
        """check if cell is already taken"""

        if self.table.get(ind) not in Game.xo:
            return True
        return False

    def check_winner(self, window: sg.Window):
        player = self.player
        opponent = self.opponent

        def check_one(player=player, opponent=opponent, window=window):
            one = 1

            if (
                self.table.get(str(one)) == player.player
                and self.table.get(str(one + 1)) == player.player
                and self.table.get(str(one + 2)) == player.player
            ):
                # check table cell 1 - 3
                window["-POPUP-"].update("You win")
                window["-RETRY-"].update(visible=True)

            if (
                self.table.get(str(one)) == player.player
                and self.table.get(str(one + 3)) == player.player
                and self.table.get(str(one + 6)) == player.player
            ):
                # check table cell 1 - 9
                window["-POPUP-"].update("You win")
                window["-RETRY-"].update(visible=True)

            if (
                self.table.get(str(one)) == player.player
                and self.table.get(str(one + 4)) == player.player
                and self.table.get(str(one + 8)) == player.player
            ):
                # check table cell 1 - 7
                window["-POPUP-"].update("You win")
                window["-RETRY-"].update(visible=True)

            if (
                self.table.get(str(one)) == opponent.player
                and self.table.get(str(one + 1)) == opponent.player
                and self.table.get(str(one + 2)) == opponent.player
            ):
                # check table cell 1 - 3
                window["-POPUP-"].update("You lose")
                window["-RETRY-"].update(visible=True)

            if (
                self.table.get(str(one)) == opponent.player
                and self.table.get(str(one + 3)) == opponent.player
                and self.table.get(str(one + 6)) == opponent.player
            ):
                # check table cell 1 - 9
                window["-POPUP-"].update("You lose")
                window["-RETRY-"].update(visible=True)

            if (
                self.table.get(str(one)) == opponent.player
                and self.table.get(str(one + 4)) == opponent.player
                and self.table.get(str(one + 8)) == opponent.player
            ):
                # check table cell 1 - 7
                window["-POPUP-"].update("You lose")
                window["-RETRY-"].update(visible=True)

        def check_nine(player=player, opponent=opponent, window=window):
            nine = 9

            if (
                self.table.get(str(nine)) == player.player
                and self.table.get(str(nine - 1)) == player.player
                and self.table.get(str(nine - 2)) == player.player
            ):
                # check table cell 7 - 9
                window["-POPUP-"].update("You win")
                window["-RETRY-"].update(visible=True)

            if (
                self.table.get(str(nine)) == player.player
                and self.table.get(str(nine - 3)) == player.player
                and self.table.get(str(nine - 6)) == player.player
            ):
                # check table cell 3 - 9
                window["-POPUP-"].update("You win")
                window["-RETRY-"].update(visible=True)

            if (
                self.table.get(str(nine)) == opponent.player
                and self.table.get(str(nine - 1)) == opponent.player
                and self.table.get(str(nine - 2)) == opponent.player
            ):
                # check table cell 7 - 9
                window["-POPUP-"].update("You lose")
                window["-RETRY-"].update(visible=True)

            if (
                self.table.get(str(nine)) == opponent.player
                and self.table.get(str(nine - 3)) == opponent.player
                and self.table.get(str(nine - 6)) == opponent.player
            ):
                # check table cell 3 - 9
                window["-POPUP-"].update("You lose")
                window["-RETRY-"].update(visible=True)

        def check_five(player=player, opponent=opponent, window=window):
            five = 5

            if (
                self.table.get(str(five)) == player.player
                and self.table.get(str(five - 3)) == player.player
                and self.table.get(str(five + 3)) == player.player
            ):
                # check table cell 2 - 8
                window["-POPUP-"].update("You win")
                window["-RETRY-"].update(visible=True)

            if (
                self.table.get(str(five)) == player.player
                and self.table.get(str(five - 1)) == player.player
                and self.table.get(str(five + 1)) == player.player
            ):
                # check table cell 4 - 6
                window["-POPUP-"].update("You win")
                window["-RETRY-"].update(visible=True)

            if (
                self.table.get(str(five)) == player.player
                and self.table.get(str(five - 2)) == player.player
                and self.table.get(str(five + 2)) == player.player
            ):
                # check table cell 3 - 9
                window["-POPUP-"].update("You win")
                window["-RETRY-"].update(visible=True)

            if (
                self.table.get(str(five)) == opponent.player
                and self.table.get(str(five - 3)) == opponent.player
                and self.table.get(str(five + 3)) == opponent.player
            ):
                # check table cell 2 - 8
                window["-POPUP-"].update("You lose")
                window["-RETRY-"].update(visible=True)

            if (
                self.table.get(str(five)) == opponent.player
                and self.table.get(str(five - 1)) == opponent.player
                and self.table.get(str(five + 1)) == opponent.player
            ):
                # check table cell 4 - 6
                window["-POPUP-"].update("You lose")
                window["-RETRY-"].update(visible=True)

            if (
                self.table.get(str(five)) == opponent.player
                and self.table.get(str(five - 2)) == opponent.player
                and self.table.get(str(five + 2)) == opponent.player
            ):
                # check table cell 3 - 9
                window["-POPUP-"].update("You lose")
                window["-RETRY-"].update(visible=True)

        check_one()
        check_five()
        check_nine()
        # window["-POPUP-"].update("Tie")
        # window["-RETRY-"].update(visible=True)


def main():
    # BUG buggy when going second
    game = Game()
    game_winner = game.check_winner

    layout = [
        [sg.Text(f"You'll be {game.player.player}.")],
        [sg.Text(f"You'll be {'first' if game.is_player_first() else 'second'}.")],
        [
            sg.Column(
                [
                    [
                        sg.Text(
                            game.table.get("1"),
                            key="-CELL1-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            game.table.get("4"),
                            key="-CELL4-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            game.table.get("7"),
                            key="-CELL7-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                ]
            ),
            sg.VerticalSeparator(p=((0, 0), (1, 1))),
            sg.Column(
                [
                    [
                        sg.Text(
                            game.table.get("2"),
                            key="-CELL2-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            game.table.get("5"),
                            key="-CELL5-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            game.table.get("8"),
                            key="-CELL8-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                ]
            ),
            sg.VerticalSeparator(p=((0, 0), (1, 1))),
            sg.Column(
                [
                    [
                        sg.Text(
                            game.table.get("3"),
                            key="-CELL3-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            game.table.get("6"),
                            key="-CELL6-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            game.table.get("9"),
                            key="-CELL9-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                ]
            ),
        ],
        [sg.Text(key="-POPUP-")],
        [sg.Button("Retry", k="-RETRY-", visible=False, enable_events=True)],
    ]

    window = sg.Window(title="xo", layout=layout, margins=[25, 25], size=[800, 500], finalize=True)

    while True:
        print(game.finished_game(window))
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED:
            break

        # if event == "-RETRY-":
            game = Game()
            window.refresh

        print(game.finished_game(window))
        if game.finished_game(window):

            game_winner(window)

            if game.is_player_first():

                game.player.play(game, window, event)

                game_winner(window)
                if game.finished_game(window):
                    game.opponent.play(game, window)

            else:

                game.opponent.play(game, window)

                game_winner(window)
                if game.finished_game(window):
                    game.player.play(game, window, event)

            game_winner(window)

    window.close()


if __name__ == "__main__":
    main()
