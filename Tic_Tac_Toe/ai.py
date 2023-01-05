"""tic-tac-toe ai"""
import copy as cp

from treelib import Tree


class DecisionTree(Tree):
    """tree to store game states"""

    def __init__(self, root_node, name: str, tag: str):
        super().__init__()
        self.create_node(name, tag, data=root_node)

    def update_branch_score(self, tag: str, score: int) -> None:
        """update branch score

        Args:
            tag (str): tag identifier to search for branch
            score (int): score to give the branch
        """
        self.get_node(tag).data.update_ai_score(score)


def best_move(dt: DecisionTree) -> int:
    """choose the best move from the decision tree

    Args:
         dt (DecisionTree): decision tree to search new move
    """
    root_node = dt.get_node("root_node").data
    moves = root_node.remaining_cells()
    branch_scores = [
        branch.data.ai_score
        for branch in dt.all_nodes_itr()
        if branch.identifier != "Root node" and dt.depth(branch) == 1
    ]
    best_score = max(branch_scores)
    return moves[branch_scores.index(best_score)]


def minimax(
    game,
    dt: DecisionTree | None = None,
    name="Root node",
    tag="root_node",
    # depth=0,
) -> int:
    """minimax algorithm in python

    Args:
        game (TicTacToe): game to run minimax on
        dt (DecisionTree | None, optional): decision tree to save the branches in. Defaults to None.
        name (str, optional): branch name to save in the decision tree. Defaults to "Root node".
        tag (str, optional): branch identifier to save in the decision tree. Defaults to "root_node".

    Returns:
        int: _description_
    """

    if not dt:
        dt = DecisionTree(game, name=name, tag=tag)

    if game.win():
        dt.update_branch_score(tag, -5)
        return -5
    if game.lose():
        dt.update_branch_score(tag, 5)
        return 5
    if game.tie():
        dt.update_branch_score(tag, 0)
        return 0

    branch_score: list[int] = []

    for i, cells in enumerate(game.remaining_cells()):
        branch = cp.deepcopy(game)
        bn = f"Branch {i}" if name == "Root node" else name + f"-{i}"
        bt = f"branch-{i}" if name == "Root node" else tag + f"-{i}"

        branch.set_cell(
            [
                (
                    cells,
                    game.opponent.opponent
                    if game.turn_ == "opponent"
                    else game.player.player,
                )
            ]
        )
        branch.turn()
        # branch.game_state()
        dt.create_node(bn, bt, data=branch, parent=tag)
        move = minimax(branch, dt=dt, name=bn, tag=bt)
        if move is not None:
            branch_score.append(move)

    score = min(branch_score) if game.turn_ == "player" else max(branch_score)
    if name == "Root node":
        return best_move(dt)
    dt.update_branch_score(tag, score)
    return score
