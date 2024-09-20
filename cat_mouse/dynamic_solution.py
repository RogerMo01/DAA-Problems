from graph import State, Draw
from naive import Naive
from typing import Any

class DynamicSolution(Naive):
    def __init__(self) -> None:
        self.graph = None
    

    def optimize(self, state: State) -> int:
        """Use minimax and memoization for optimization"""
        memo = {}
        return self.aux_optimize(state, memo)


    def aux_optimize(self, state: State, memo: dict) -> int:
        """Auxiliar function for optimize with memoization"""

        if state in memo:
            return memo[state]
        
        
        if isinstance(state, Draw):
            return 0
        elif state.m == 0:
            return 1
        elif state.m == state.c:
            return -1
        else:
            child_values: list[int] = []
            for adj in state.adj:
                val = self.aux_optimize(adj, memo)
                child_values.append(val)
            
            if state.m_turn:
                result = max(child_values)
            if state.c_turn:
                result = min(child_values)


        memo[state] = result
        return result
