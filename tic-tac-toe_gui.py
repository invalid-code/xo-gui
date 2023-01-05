#!/usr/bin/env python

import re

import PySimpleGUI as sg

from Tic_Tac_Toe.game import TicTacToe

# from Tic_Tac_Toe.players import Player, Opponent

sg.theme("dark grey")


def main():
    # BUG buggy when going second
    game = TicTacToe()

    layout = [
        [sg.Text(f"You'll be {game.player.player}.")],
        [sg.Text(f"You'll be {'first' if game.first_mover() else 'second'}.")],
        [
            sg.Column(
                [
                    [
                        sg.Text(
                            text=game.get_cell(0, " "),
                            key="-CELL1-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            text=game.get_cell(3, " "),
                            key="-CELL4-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            text=game.get_cell(6, " "),
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
                            text=game.get_cell(1, " "),
                            key="-CELL2-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            text=game.get_cell(4, " "),
                            key="-CELL5-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            text=game.get_cell(7, " "),
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
                            text=game.get_cell(2, " "),
                            key="-CELL3-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            text=game.get_cell(5, " "),
                            key="-CELL6-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            text=game.get_cell(8, " "),
                            key="-CELL9-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                ]
            ),
        ],
        [sg.Text(key="-POPUP-")],
        [
            sg.Button(
                "Retry",
                k="-RETRY-",
                visible=False,
                enable_events=False,
            )
        ],
    ]

    window = sg.Window(
        title="xo", layout=layout, margins=[25, 25], size=[200, 250], finalize=True
    )

    while True:
        event, _ = window.read()

        if event == sg.WIN_CLOSED:
            break

        # if event == "-RETRY-":
        # game = TicTacToe()
        # window.refresh

        tie = game.tie
        win = game.win
        lose = game.lose

        if re.search(r"-CELL[1-9]-", event):
            if game.first_mover():

                #  pylint: disable=E1121
                game.player.play(event, game, window)

                if win():
                    window["-POPUP-"].update("Win")
                    window["-RETRY-"].update(visible=True)

                if lose():
                    window["-POPUP-"].update("Lose")
                    window["-RETRY-"].update(visible=True)

                if tie():
                    window["-POPUP-"].update("Tie")
                    window["-RETRY-"].update(visible=True)

                game.opponent.play(game, window)

            else:

                pass
                # game.opponent.play(game, window)

                # if win():
                #     window["-POPUP-"].update("Win")
                #     window["-RETRY-"].update(visible=True)

                # if lose():
                #     window["-POPUP-"].update("Lose")
                #     window["-RETRY-"].update(visible=True)

                # if tie():
                #     window["-POPUP-"].update("Tie")
                #     window["-RETRY-"].update(visible=True)

                # player_play: dict = game.player.play(game, event)
                # if player_play:
                #     window[player_play.get("cell")].update(game.player.player)

            if tie():
                window["-POPUP-"].update("Tie")
                window["-RETRY-"].update(visible=True)

            if win():
                window["-POPUP-"].update("Win")
                window["-RETRY-"].update(visible=True)

            if lose():
                window["-POPUP-"].update("Lose")
                window["-RETRY-"].update(visible=True)

    window.close()


if __name__ == "__main__":
    main()
