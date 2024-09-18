from graph import Graph, State, Draw
from naive import Naive
from typing import Any


class DynamicSolution(Naive):
    def __init__(self) -> None:
        self.graph = None
    

    def optimize(self, state: State, memo = {}) -> int:
        """Use minimax and memoization for optimization"""

        if state in memo:
            return memo[state]
        
        minmax = super().optimize(state)

        memo[state] = minmax
        return minmax
