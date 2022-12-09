import copy as cp


class DecisionTree:
    def __init__(self, root_node):
        self.decision_tree: list[list] = []
        if len(self.decision_tree) == 0:
            self.update_decision_tree([root_node])

    def __repr__(self) -> str:
        return f"DecisionTree(decision_tree='{self.decision_tree}')"

    def __str__(self):
        from pprint import pformat

        return pformat(vars(self), indent=4, width=1)

    def update_decision_tree(
        self, branches: list, parent_branch: tuple[int, int] | None = None
    ):
        # if parent_branch is None:
        # return None
        self.decision_tree.append(branches)
        # self.decision_tree.append([branches])

    def update_branch_score(self, coordinates: tuple[int, int], score: int):
        """update branch score

        Args:
            coordinates (tuple[int, int]): to find where branch is located
            score (int): score to give the branch
        """
        pass


def best_move(decision_tree: DecisionTree):
    """_summary_

    Args:
        decision_tree (DecisionTree): _description_
    """
    pass


def minimax(
    game,
    depth=0,
):
    # TODO: go backwards to the decision tree and give score
    # * no recursion implementation of minimax alg

    next_row = []
    decision_tree = DecisionTree(game)

    for row_i, row in enumerate(decision_tree.decision_tree):
        for branch_i, branch in enumerate(row):
            if branch.win():
                # decision_tree.update_branch_score((row_i, branch_i), 1)
                break
            elif branch.lose():
                # decision_tree.update_branch_score((row_i, branch_i), -1)
                break
            elif branch.tie():
                # decision_tree.update_branch_score((row_i, branch_i), 0)
                break
            for i, cell in enumerate(branch.table):
                if branch.cell(i):
                    game_branch = cp.deepcopy(branch)
                    game_branch.set_cell(
                        [
                            (
                                i,
                                game_branch.opponent.player
                                if branch.turn_ == branch.opponent.name
                                else game_branch.player.player,
                            )
                        ]
                    )
                    game_branch.turn()
                    next_row.append(game_branch)
            decision_tree.update_decision_tree(next_row, (row_i, branch_i))
            next_row = []
    print(decision_tree)
