class Graph:
    def __init__(self, adjacency_list: dict[int, list[int]]) -> None:
        self.adj = adjacency_list

    def __getitem__(self, index: int):
        return self.adj[index]
    
    def list_nodes(self):
        return [x[0] for x in self.adj.items()]
    
    def list_edges(self):
        for u, l in self.adj.items():
            for v in l:
                if u < v: yield (u, v)

    def __len__(self):
        return len(self.adj)
    
    def __str__(self) -> str:
        return f"{self.adj}\n"
    