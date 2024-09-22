from graph import Graph
from typing import Any, Generator
from itertools import combinations, permutations

class Naive:

    def __call__(self, graph: Graph, k: int) -> Any:
        """Calculates the result"""

        if k < 0: raise Exception("k: cannot be less than 0")
        if k > len(graph): return False
        if k == 0: return len(graph) > 0

        nodes = graph.list_nodes()

        # Check linear paths
        if k < len(graph):
            combs = combinations(nodes, k+1)

            # Check for each subset of V
            for comb in combs:
                for potential_path in permutations(comb):
                    potential_path = list(potential_path)
                    if self.is_path(potential_path, graph): return True


        # Check cycle paths
        if k > 2:
            combs = combinations(nodes, k)

            # Check for each subset of V
            for comb in combs:
                for potential_path in permutations(comb):
                    potential_path = list(potential_path)
                    potential_path.append(potential_path[0])
                    if self.is_path(potential_path, graph): return True

        return False
    
    
    
    def is_path(self, vertex_order: Generator, graph: Graph):
        """Checks if the sequence represent a path in the given graph"""

        for i in range(0, len(vertex_order)-1):
            u = vertex_order[i]
            v = vertex_order[i+1]

            if not v in graph[u]:
                return False
        
        path = f"{vertex_order[0]} "
        for i in range(len(vertex_order)): 
            if i != 0: path += f"➡  {vertex_order[i]} "
        print(f"K-Path: {path}")
        return True
    
