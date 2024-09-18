from graph import Graph, State, Draw
from typing import Any


class Naive:
    def __init__(self) -> None:
        self.graph = None

    def __call__(self, graph: Graph) -> Any:
        """Calculates the result"""

        self.graph = graph

        DAG: State = State(1, 2, True)
        
        d: dict[State, State] = {}
        f: set[State] = set()
        
        # Build DAG
        self.visit(DAG, d, f)

        value = self.optimize(DAG)
        return value
    


    def visit(self, state: State, d: dict[State, State], f: set[State]):
        """Builds Mouse-Cat game states DAG"""

        d[state] = state

        if isinstance(state, Draw) or state.m == 0 or state.m == state.c:
            pass

        else:
            # Mouse turn
            if state.m_turn:
                for a in self.graph[state.m]:
                    # Take instance if already exists
                    new_state = State(a, state.c, False)
                    if new_state in d: new_state = d[new_state]

                    if new_state in d and not new_state in f:
                        new_state = Draw(new_state.m, new_state.c, new_state.m_turn)
                    
                    state.append_adj(new_state)

                    if new_state not in f:
                        self.visit(new_state, d, f)

            # Cat turn
            else:
                for a in self.graph[state.c]:
                    if a == 0: continue
                    # Take instance if already exists
                    new_state = State(state.m, a, True)
                    if new_state in d: new_state = d[new_state]

                    if new_state in d and not new_state in f:
                        new_state = Draw(new_state.m, new_state.c, new_state.m_turn)

                    state.append_adj(new_state)

                    if new_state not in f:
                        self.visit(new_state, d, f)

        f.add(state)



    def optimize(self, state: State) -> int:
        """Use minimax for optimization"""

        if isinstance(state, Draw):
            return 0
        elif state.m == 0:
            return 1
        elif state.m == state.c:
            return -1
        else:
            child_values: list[int] = []
            for adj in state.adj:
                val = self.optimize(adj)
                child_values.append(val)
            
            if state.m_turn:
                return max(child_values)
            if state.c_turn:
                return min(child_values)
