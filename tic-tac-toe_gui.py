#!/usr/bin/env python

import PySimpleGUI as sg

from back import Tic_Tac_Toe

sg.theme("dark grey")


def main():
    # BUG buggy when going second
    game = Tic_Tac_Toe()

    layout = [
        [sg.Text(f"You'll be {game.player.player}.")],
        [sg.Text(f"You'll be {'first' if game.first_mover() else 'second'}.")],
        [
            sg.Column(
                [
                    [
                        sg.Text(
                            text=game.table.get("1"),
                            key="-CELL1-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            text=game.table.get("4"),
                            key="-CELL4-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            text=game.table.get("7"),
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
                            text=game.table.get("2"),
                            key="-CELL2-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            text=game.table.get("5"),
                            key="-CELL5-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            text=game.table.get("8"),
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
                            text=game.table.get("3"),
                            key="-CELL3-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            text=game.table.get("6"),
                            key="-CELL6-",
                            enable_events=True,
                            size=[1, 1],
                        )
                    ],
                    [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
                    [
                        sg.Text(
                            text=game.table.get("9"),
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
            game = Tic_Tac_Toe()
            window.refresh

        # if game.tie():
        #     window["-POPUP-"].update("Tie")
        #     window["-RETRY-"].update(visible=True)
        tie = game.tie
        win = game.win
        lose = game.lose

        if game.first_mover():

            player_play: dict = game.player.play(event)
            if player_play:
                window[player_play.get("cell")].update(game.player.player)

            if win():
                window["-POPUP-"].update("Win")
                window["-RETRY-"].update(visible=True)

            if lose():
                window["-POPUP-"].update("Lose")
                window["-RETRY-"].update(visible=True)

            if tie():
                window["-POPUP-"].update("Tie")
                window["-RETRY-"].update(visible=True)

            game.opponent.play()

        else:

            game.opponent.play(game, window)

            if win():
                window["-POPUP-"].update("Win")
                window["-RETRY-"].update(visible=True)

            if lose():
                window["-POPUP-"].update("Lose")
                window["-RETRY-"].update(visible=True)

            if tie():
                window["-POPUP-"].update("Tie")
                window["-RETRY-"].update(visible=True)

            player_play: dict = game.player.play(game, event)
            if player_play:
                window[player_play.get("cell")].update(game.player.player)

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
