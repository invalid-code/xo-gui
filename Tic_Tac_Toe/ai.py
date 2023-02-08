"""tic-tac-toe ai"""
from treelib import Tree
import copy as cp



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


def calculate_branch(name, tag, game, cells, i, branch_score, dt) -> None:
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
    dt.create_node(bn, bt, data=branch, parent=tag)
    move = minimax(branch, dt=dt, name=bn, tag=bt)
    if move is not None:
        branch_score.append(move)


def best_move(dt: DecisionTree) -> int:
    """choose the best move from the decision tree

    Args:
         dt (DecisionTree): decision tree to
          new move
    """
    # dt.show(data_property="ai_score")
    root_node = dt.get_node("root_node")
    branches = dt.children(root_node.identifier)
    moves = root_node.data.remaining_cells()
    branch_scores = [branch.data.ai_score for branch in branches]
    print(branch_scores)
    best_score = max(branch_scores)
    return moves[branch_scores.index(best_score)]


def minimax(
    game,
    dt: DecisionTree | None = None,
    name="Root node",
    tag="root_node",
) -> int:
    """minimax algorithm in python

    Args:
        game (TicTacToe): game to run minimax on
        dt (DecisionTree | None, optional): decision tree to save the branches in. Defaults to None.
        name (str, optional): branch name to save in the decision tree. Defaults to "Root node".
        tag (str, optional): branch identifier to save in the decision tree. Defaults to "root_node".

    Returns:
        int: index of move to make
    """
    if not dt:
        dt = DecisionTree(game, name=name, tag=tag)

    terminal_state = game.terminal_state()
    if terminal_state[0]:
        dt.update_branch_score(tag, terminal_state[1])
        return terminal_state[1]

    branch_score: list[int] = []

    for i, cells in enumerate(game.remaining_cells()):
        calculate_branch(name, tag, game, cells, i, branch_score, dt)

    if name == "Root node":
        return best_move(dt)
    score = min(branch_score) if game.turn_ == "player" else max(branch_score)
    dt.update_branch_score(tag, score)
    return score
