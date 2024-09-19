from graph import State, Draw
from naive import Naive
from typing import Any


class BestSolution(Naive):
    def __init__(self) -> None:
        self.graph = None
    

    def optimize(self, state: State, memo = {}) -> int:
        """Use minimax, memoization and pruning for optimization"""
        memo = {}
        return self.aux_optimize(state, memo)
        
    
    def aux_optimize(self, state: State, memo: dict) -> int:
        """Auxiliar function for optimize with memoization and pruning"""

        if state in memo:
            return memo[state]
        
        
        if isinstance(state, Draw):
            return 0
        elif state.m == 0:
            return 1
        elif state.m == state.c:
            return -1
        else:
            max = -1
            min = 1
            for adj in state.adj:
                val = self.aux_optimize(adj, memo)

                if state.m_turn:
                    # Pruning for max value achieved
                    if val == 1:
                        max = 1
                        break
                    # Continue searching
                    if val > max: max = val

                if state.c_turn:
                    # Pruning for min value achieved
                    if val == -1:
                        min = -1
                        break
                    # Continue searching
                    if val < min: min = val

            if state.m_turn:
                result = max
            if state.c_turn:
                result = min
            

        memo[state] = result
        return result
