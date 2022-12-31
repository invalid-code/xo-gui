"""tic-tac-toe ai"""
import copy as cp
from treelib import Tree
from .game import TicTacToe

# from .players import Player


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
        self.get_node(tag).data.update_ai_score(score)


def best_move(decision_tree: DecisionTree) -> int:
    """choose the best move from the decision tree

    Args:
         decision_tree (DecisionTree): decision tree to search new move
    """
    root_node = decision_tree.get_node("root_node").data
    moves = root_node.remaining_cells()
    branch_scores = [
        branch.data.ai_score
        for branch in decision_tree.all_nodes_itr()
        if branch.identifier != "Root node" and decision_tree.depth(branch) == 1
    ]
    best_score = max(branch_scores)
    return moves[branch_scores.index(best_score)]


def minimax(
    game: TicTacToe,
    decision_tree: DecisionTree | None = None,
    name="Root node",
    tag="root_node",
    # depth=0,
) -> int:

    if not decision_tree:
        decision_tree = DecisionTree(game, name=name, tag=tag)

    if game.win():
        decision_tree.update_branch_score(tag, -5)
        return -5
    if game.lose():
        decision_tree.update_branch_score(tag, 5)
        return 5
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
                    game.opponent.opponent
                    if game.turn_ == "opponent"
                    else game.player.player,
                )
            ]
        )
        branch.turn()
        # branch.game_state()
        decision_tree.create_node(branch_name, branch_tag, data=branch, parent=tag)
        move = minimax(
            branch, decision_tree=decision_tree, name=branch_name, tag=branch_tag
        )
        if move is not None:
            branch_score.append(move)
    score = min(branch_score) if game.turn_ == "player" else max(branch_score)
    if name == "Root node":
        return best_move(decision_tree)
    decision_tree.update_branch_score(tag, score)
    return score
