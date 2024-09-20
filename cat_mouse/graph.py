

from typing import Any


class Graph:
    def __init__(self, adjacency_list: dict[int, list[int]]) -> None:
        self.adj = adjacency_list

    def __getitem__(self, index: int):
        return self.adj[index]
    
    def list_nodes(self):
        return [x[0] for x in self.adj.items()]
    


class State:
    def __init__(self, m: int, c: int, m_turn: bool) -> None:
        self.m = m
        self.c = c
        self.m_turn = m_turn
        self.c_turn = not m_turn
        self.color = None

        self.adj: list[State] = []


    def append_adj(self, state: 'State'):
        self.adj.append(state)

    def __hash__(self) -> int:
        return hash(repr(self))

    def __eq__(self, value: 'State') -> bool:
        return self.m == value.m and self.c == value.c and self.m_turn == value.m_turn

    def __repr__(self) -> str:
        return f"({self.m}, {self.c}, {self.m_turn})"
        
    def __str__(self) -> str:
        return f"""({self.m}, {self.c}, {self.m_turn})
        {self.adj}
        """


class Draw(State):
    def __init__(self, m, c, m_turn):
        super().__init__(m, c, m_turn)

    
    def __hash__(self) -> int:
        return hash(f"Draw ({self.m}, {self.c}, {self.m_turn})")
        
    def __eq__(self, value: State) -> bool:
        return super().__eq__(value) and isinstance(self, Draw) and isinstance(value, Draw)

    def __repr__(self) -> str:
        return f"Draw ({self.m}, {self.c}, {self.m_turn})"
        
    def __str__(self) -> str:
        return f"Draw ({self.m}, {self.c}, {self.m_turn})"
