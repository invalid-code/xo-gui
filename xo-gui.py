#!/usr/bin/env python

import random as rd

import PySimpleGUI as sg

sg.theme("dark grey")


class Player:
    def __init__(self, player_avatar: str, is_player_opponent: str):
        self.player = player_avatar
        self.is_player_opponent = is_player_opponent

    def play(self, ind: str, game):
        if game.check_cell(ind):
            game.table[ind] = self.player
            return True
        return False

    def __repr__(self):
        return f"Player(player={self.player}, is_player_opponent={self.is_player_opponent})"

    def __str__(self):
        return f"player is {self.player}\nplayer is the {self.is_player_opponent}"


class PlayerA(Player):
    pass


class PlayerB(Player):
    def play(self, game):
        ind = ""
        # temporary
        for key, cell in game.table.items():
            if not cell:
                game.table[key] = self.player
                return {"has_played": True, "cell": key}


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

    def get_cell_value(self, ind: str):
        return self.table.get(ind)

    def is_player_first(self):
        if self.first == self.player.player:
            return True
        return False

    def finished_game(self, window):
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

    def check_winner(self, window):
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

    def __repr__(self):
        return f"Game(player_avatar={self.player_avatar}, player={self.player.__repr__()}, opponent={self.opponent.__repr__()}, first={self.first}, table={self.table})"

    def __str__(self):
        return f"the player's avatar will be {self.player_avatar}\nplayer will be {self.player}\nopponent will be {self.opponent}\n {self.player if self.first else self.opponent}\n {self.table} will be playing field"


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

    window = sg.Window(title="xo", layout=layout, margins=[25, 25], size=[800, 500])

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

            # if event == "-RETRY-":
            game = Game()
            window.refresh

        game_winner(window)
        if game.finished_game(window):
            if game.is_player_first():
                if event == "-CELL1-":
                    if game.player.play("1", game):
                        window[event].update(game.player.player)
                if event == "-CELL2-":
                    if game.player.play("2", game):
                        window[event].update(game.player.player)
                if event == "-CELL3-":
                    if game.player.play("3", game):
                        window[event].update(game.player.player)
                if event == "-CELL4-":
                    if game.player.play("4", game):
                        window[event].update(game.player.player)
                if event == "-CELL5-":
                    if game.player.play("5", game):
                        window[event].update(game.player.player)
                if event == "-CELL6-":
                    if game.player.play("6", game):
                        window[event].update(game.player.player)
                if event == "-CELL7-":
                    if game.player.play("7", game):
                        window[event].update(game.player.player)
                if event == "-CELL8-":
                    if game.player.play("8", game):
                        window[event].update(game.player.player)
                if event == "-CELL9-":
                    if game.player.play("9", game):
                        window[event].update(game.player.player)

                game_winner(window)
                if game.finished_game(window):
                    play_opponent = game.opponent.play(game, window)
                    # if play_opponent.get("has_played"):
                    #     window[f"-CELL{play_opponent.get('cell')}-"].update(
                    #         game.opponent.player
                    #     )
            else:
                play_opponent = game.opponent.play(game)
                if play_opponent.get("has_played"):
                    window[f"-CELL{play_opponent.get('cell')}-"].update(
                        game.opponent.player
                    )
                    window.refresh()

                game_winner(window)
                if game.finished_game(window):
                    if event == "-CELL1-":
                        if game.player.play("1", game):
                            window[event].update(game.player.player)
                    if event == "-CELL2-":
                        if game.player.play("2", game):
                            window[event].update(game.player.player)
                    if event == "-CELL3-":
                        if game.player.play("3", game):
                            window[event].update(game.player.player)
                    if event == "-CELL4-":
                        if game.player.play("4", game):
                            window[event].update(game.player.player)
                    if event == "-CELL5-":
                        if game.player.play("5", game):
                            window[event].update(game.player.player)
                    if event == "-CELL6-":
                        if game.player.play("6", game):
                            window[event].update(game.player.player)
                    if event == "-CELL7-":
                        if game.player.play("7", game):
                            window[event].update(game.player.player)
                    if event == "-CELL8-":
                        if game.player.play("8", game):
                            window[event].update(game.player.player)
                    if event == "-CELL9-":
                        if game.player.play("9", game):
                            window[event].update(game.player.player)

        game_winner(window)

    window.close()


if __name__ == "__main__":
    main()
