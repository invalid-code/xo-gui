#!/usr/bin/env python

import re

import PySimpleGUI as sg

from Tic_Tac_Toe.game import TicTacToe


sg.theme("dark grey")


def main():
    # BUG buggy when going second
    game = TicTacToe()

    print(game)

    start_menu: list[list[sg.Text | sg.Button]] = [
        [sg.Text("Tic-Tac-Toe", k="-TITLE-")],
        [sg.Button("Play", k="-PLAY-"), sg.Text("v.s. Ai", k="-VSAI-")],
    ]

    info: list[list[sg.Text]] = [
        [
            sg.Text(
                f"You'll be {game.player.player}.",
                k="-XO-",
            )
        ],
        [
            sg.Text(
                f"You'll be {'first' if game.first_mover() == 'player' else 'second'}.",
                k="-MOVE-",
            )
        ],
    ]

    tic_tac_toe_game: list[list[sg.Text | sg.HorizontalSeparator | sg.VerticalSeparator]] = [
        [
            sg.Text(
                text=game.get_cell(0, " "),
                key="-CELL1-",
                enable_events=True,
                size=[1, 1],
            ),
            sg.VerticalSeparator(),
            sg.Text(
                text=game.get_cell(1, " "),
                key="-CELL2-",
                enable_events=True,
                size=[1, 1],
            ),
            sg.VerticalSeparator(),
            sg.Text(
                text=game.get_cell(2, " "),
                key="-CELL3-",
                enable_events=True,
                size=[1, 1],
            ),
        ],
        [sg.HorizontalSeparator()],
        [
            sg.Text(
                text=game.get_cell(3, " "),
                key="-CELL4-",
                enable_events=True,
                size=[1, 1],
            ),
            sg.VerticalSeparator(),
            sg.Text(
                text=game.get_cell(4, " "),
                key="-CELL5-",
                enable_events=True,
                size=[1, 1],
            ),
            sg.VerticalSeparator(),
            sg.Text(
                text=game.get_cell(5, " "),
                key="-CELL6-",
                enable_events=True,
                size=[1, 1],
            ),
        ],
        [sg.HorizontalSeparator()],
        [
            sg.Text(
                text=game.get_cell(6, " "),
                key="-CELL7-",
                enable_events=True,
                size=[1, 1],
            ),
            sg.VerticalSeparator(),
            sg.Text(
                text=game.get_cell(7, " "),
                key="-CELL8-",
                enable_events=True,
                size=[1, 1],
            ),
            sg.VerticalSeparator(),
            sg.Text(
                text=game.get_cell(8, " "),
                key="-CELL9-",
                enable_events=True,
                size=[1, 1],
            ),
        ],
    ]

    # tic_tac_toe_game = [
    #     sg.Column(
    #         [
    #             [
    #                 sg.Text(
    #                     text=game.get_cell(0, " "),
    #                     key="-CELL1-",
    #                     enable_events=True,
    #                     size=[1, 1],
    #                     visible=False,
    #                 )
    #             ],
    #             [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
    #             [
    #                 sg.Text(
    #                     text=game.get_cell(3, " "),
    #                     key="-CELL4-",
    #                     enable_events=True,
    #                     size=[1, 1],
    #                     visible=False,
    #                 )
    #             ],
    #             [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
    #             [
    #                 sg.Text(
    #                     text=game.get_cell(6, " "),
    #                     key="-CELL7-",
    #                     enable_events=True,
    #                     size=[1, 1],
    #                     visible=False,
    #                 )
    #             ],
    #         ]
    #     ),
    #     sg.VerticalSeparator(p=((0, 0), (1, 1))),
    #     sg.Column(
    #         [
    #             [
    #                 sg.Text(
    #                     text=game.get_cell(1, " "),
    #                     key="-CELL2-",
    #                     enable_events=True,
    #                     size=[1, 1],
    #                     visible=False,
    #                 )
    #             ],
    #             [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
    #             [
    #                 sg.Text(
    #                     text=game.get_cell(4, " "),
    #                     key="-CELL5-",
    #                     enable_events=True,
    #                     size=[1, 1],
    #                     visible=False,
    #                 )
    #             ],
    #             [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
    #             [
    #                 sg.Text(
    #                     text=game.get_cell(7, " "),
    #                     key="-CELL8-",
    #                     enable_events=True,
    #                     size=[1, 1],
    #                     visible=False,
    #                 )
    #             ],
    #         ]
    #     ),
    #     sg.VerticalSeparator(p=((0, 0), (1, 1))),
    #     sg.Column(
    #         [
    #             [
    #                 sg.Text(
    #                     text=game.get_cell(2, " "),
    #                     key="-CELL3-",
    #                     enable_events=True,
    #                     size=[1, 1],
    #                     visible=False,
    #                 )
    #             ],
    #             [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
    #             [
    #                 sg.Text(
    #                     text=game.get_cell(5, " "),
    #                     key="-CELL6-",
    #                     enable_events=True,
    #                     size=[1, 1],
    #                     visible=False,
    #                 )
    #             ],
    #             [sg.HorizontalSeparator(p=((0, 0), (1, 1)))],
    #             [
    #                 sg.Text(
    #                     text=game.get_cell(8, " "),
    #                     key="-CELL9-",
    #                     enable_events=True,
    #                     size=[1, 1],
    #                     visible=False,
    #                 )
    #             ],
    #         ]
    #     ),
    # ]

    layout = [
        [sg.Column(start_menu, visible=True, k="-START MENU-"), sg.Column(info, visible=False, k="-INFO-"),
         ],
        [sg.Column(tic_tac_toe_game, visible=False, k="-GAME-")],
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
        title="xo",
        layout=layout,
        margins=[25, 25],
        size=[200, 250],
        finalize=True,
    )

    while True:
        event, values = window.read()

        print(event)

        if event == sg.WIN_CLOSED:
            break

        if event == "-PLAY-":
            window["-START MENU-"].update(visible=False)
            window["-INFO-"].update(visible=True)
            window["-GAME-"].update(visible=True)
            window.refresh()

            if game.first_mover() == "opponent":
                game.opponent.play(game, window)

        if event == "-RETRY-":
            game = TicTacToe()
            for i in range(1, 10):
                window[f"-CELL{i}-"].update(game.get_cell(i-1))
            window[event].update(visible=False)
            window["-POPUP-"].update(visible=False)
            window["-XO-"].update(f"You'll be {game.player.player}.")
            window["-MOVE-"].update(
                f"You'll be {'first' if game.first_mover() == 'player' else 'second'}."
            )
            window.refresh()

        if re.search(r"-CELL[1-9]-", event):

            game.player.play(event, game, window)

            terminal_state = game.terminal_state()
            if terminal_state[0]:
                match terminal_state[1]:
                    case 5:
                        window["-POPUP-"].update("Win")
                        window["-RETRY-"].update(visible=True)
                    case -5:
                        window["-POPUP-"].update("Lose")
                        window["-RETRY-"].update(visible=True)
                    case 0:
                        window["-POPUP-"].update("Tie")
                        window["-RETRY-"].update(visible=True)
            else:
                game.opponent.play(game, window)

            terminal_state = game.terminal_state()
            if terminal_state[0]:
                match terminal_state[1]:
                    case 5:
                        window["-POPUP-"].update("Win")
                        window["-RETRY-"].update(visible=True)
                    case -5:
                        window["-POPUP-"].update("Lose")
                        window["-RETRY-"].update(visible=True)
                    case 0:
                        window["-POPUP-"].update("Tie")
                        window["-RETRY-"].update(visible=True)

    window.close()


if __name__ == "__main__":
    main()
