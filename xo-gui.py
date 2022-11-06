#!/usr/bin/env python

import random as rd
import copy as cp
from back import Game

import PySimpleGUI as sg

sg.theme("dark grey")


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

    window = sg.Window(
        title="xo", layout=layout, margins=[25, 25], size=[800, 500], finalize=True
    )

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

            # if event == "-RETRY-":
            game = Game()
            window.refresh

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
