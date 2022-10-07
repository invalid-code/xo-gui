#!/usr/bin/env python

import random as rd

import PySimpleGUI as sg

sg.theme("dark grey")


class Player:
    def __init__(self, is_first):
        self.is_first = True if is_first else False
        self.player = rd.choice(Game.xo)

    def play(self, ind: str, game):

        if game.check_cell(ind):
            game.table[ind] = self.player
            return True


class Opponent:
    def __init__(self, player, is_first):
        self.is_first = True if not is_first else False
        self.opponent = "X" if player.player == "O" else "O"

    def play(self, game):
        cell = ""
        opponent_status = {"cell": ""}

        # ai
        # 

        if game.check_cell(cell):
            game.table[cell] = self.opponent
            opponent_status.update({"cell": cell, "has_played": True})
        
        return opponent_status


class Game:
    xo = ("X", "O")

    def __init__(self):
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
    
    def get_cell_value(self, ind:str):
        return self.table.get(ind)

    def is_player_first(self):
        if self.first == Game.xo[0]:
            return True
        return False

    def finished_game(self):
        """To check if game is finished"""

        for cell in self.table.values():

            if cell not in Game.xo:  # if a cell has no value return true
                return True

        return False

    def check_cell(self, ind: str):
        """check if cell is already taken"""

        if self.table.get(ind) not in Game.xo:
            return True

        return False

    def check_winner(self, player: Player, opponent: Opponent):
        """To check if someone has alredy won"""
        status = {"is_winner": ""}

        def check_one(status=status, player=player, opponent=opponent):
            one = 1

            if (
                self.table.get(str(one)) == player.player
                and self.table.get(str(one + 1)) == player.player
                and self.table.get(str(one + 2)) == player.player
            ):
                status.update({"is_winner": "win", "player": player.player})
                return status

            if (
                self.table.get(str(one)) == player.player
                and self.table.get(str(one + 3)) == player.player
                and self.table.get(str(one + 6)) == player.player
            ):
                status.update({"is_winner": "win", "player": player.player})
                return status

            return status

        def check_nine(status=status, player=player, opponent=opponent):
            nine = 9

            if (
                self.table.get(str(nine)) == player.player
                and self.table.get(str(nine - 1)) == player.player
                and self.table.get(str(nine - 2)) == player.player
            ):
                status.update({"is_winner": "win", "player": player.player})
                return status

            if (
                self.table.get(str(nine)) == player.player
                and self.table.get(str(nine - 3)) == player.player
                and self.table.get(str(nine - 6)) == player.player
            ):
                status.update({"is_winner": "win", "player": player.player})
                return status

            return status

        def check_five(status=status, player=player, opponent=opponent):
            pass

        one = check_one()
        if one.get("is_winner"):
            return one

        # five = check_five()
        # if five.get("is_winner"):
        #     return five

        nine = check_nine()
        if nine.get("is_winner"):
            return nine

        return status


def main():
    game = Game()
    is_first = game.is_player_first()
    player = Player(is_first)
    opponent = Opponent(player, is_first)

    layout = [
        [sg.Text(f"You'll be {player.player}.")],
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
        game_winner = game.check_winner

        if event == sg.WIN_CLOSED:
            break

        if event == "-RETRY-":
            game = Game()
            # window.refresh

        if not game.check_winner(player, opponent).get("is_winner"):
            if game.finished_game():
                if player.is_first:
                    if event == "-CELL1-":
                        if player.play("1", game):
                            window[event].update(player.player)
                    if event == "-CELL2-":
                        if player.play("2", game):
                            window[event].update(player.player)
                    if event == "-CELL3-":
                        if player.play("3", game):
                            window[event].update(player.player)
                    if event == "-CELL4-":
                        if player.play("4", game):
                            window[event].update(player.player)
                    if event == "-CELL5-":
                        if player.play("5", game):
                            window[event].update(player.player)
                    if event == "-CELL6-":
                        if player.play("6", game):
                            window[event].update(player.player)
                    if event == "-CELL7-":
                        if player.play("7", game):
                            window[event].update(player.player)
                    if event == "-CELL8-":
                        if player.play("8", game):
                            window[event].update(player.player)
                    if event == "-CELL9-":
                        if player.play("9", game):
                            window[event].update(player.player)

                    play_opponent = opponent.play(game)
                    if play_opponent.get("has_played"):
                        window[play_opponent.get("cell")].update(opponent.opponent)

                if opponent.is_first:
                    pass

        if game_winner(player, opponent).get("is_winner") == "win":
            window["-POPUP-"].update("You win")
            window["-RETRY-"].update(visible=True)

        if game_winner(player, opponent).get("is_winner") == "lose":
            window["-POPUP-"].update("You lose")
            window["-RETRY-"].update(visible=True)

        if game_winner(player, opponent).get("is_winner") == "tie":
            window["-POPUP-"].update("Tie")
            window["-RETRY-"].update(visible=True)

    window.close()


if __name__ == "__main__":
    main()
