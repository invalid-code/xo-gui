import copy as cp
from treelib import Tree
from .game import TicTacToe
from .players import Player


class DecisionTree(Tree):
    """tree to store game states"""

    def __init__(self, root_node: TicTacToe, name: str, tag: str):
        super().__init__()
        self.create_node(name, tag, data=root_node)

    def update_branch_score(self, tag: str, score: int) -> None:
        """update branch score

        Args:
            tag (str): tag identifier to search for branch
            score (int): score to give the branch
        """
        # print(self.update_node(tag))
        self.get_node(tag).data.update_ai_score(score)


def best_move(decision_tree: DecisionTree):
    """_summary_

    Args:
         decision_tree (DecisionTree): _description_
    """


def minimax(
    game: TicTacToe,
    decision_tree: DecisionTree | None = None,
    name="Root node",
    tag="root_node",
    depth=0,
) -> int | None:

    if not decision_tree:
        decision_tree = DecisionTree(game, name=name, tag=tag)

    if game.win():
        decision_tree.update_branch_score(tag, 1)
        return 1
    if game.lose():
        decision_tree.update_branch_score(tag, -1)
        return -1
    if game.tie():
        decision_tree.update_branch_score(tag, 0)
        return 0

    branch_score: list[int] = []

    for branch_i, remaining_cell_i in enumerate(game.remaining_cells()):
        branch = cp.deepcopy(game)
        branch_name = (
            f"Branch {branch_i}" if name == "Root node" else name + f"-{branch_i}"
        )
        branch_tag = (
            f"branch-{branch_i}" if name == "Root node" else tag + f"-{branch_i}"
        )
        branch.set_cell(
            [
                (
                    remaining_cell_i,
                    Player.xo[0] if game.turn_ == "opponent" else Player.xo[1],
                )
            ]
        )
        branch.turn()
        # branch.game_state()
        decision_tree.create_node(branch_name, branch_tag, data=branch, parent=tag)
        move = minimax(
            branch, decision_tree=decision_tree, name=branch_name, tag=branch_tag
        )
        if move:
            branch_score.append(move)
    decision_tree.show(data_property="ai_score")
    score = max(branch_score) if game.turn_ == "player" else min(branch_score)
    decision_tree.update_branch_score(tag, score)
    return score
