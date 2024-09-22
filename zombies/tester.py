from graph import Graph
from naive import Naive

g = Graph({
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
})

g = Graph({
    0: [2, 4],
    1: [2, 3],
    2: [0, 1, 3],
    3: [1, 2],
    4: [0]
})


g = Graph({
    0: []
})

g = Graph({
    0: [1, 3, 4],
    1: [0, 2],
    2: [1],
    3: [0, 4],
    4: [0, 3]
})

g = Graph({
    0: [1],
    1: [2],
    2: [3],
    3: [4],
    4: [0]
})




k = 5

naive = Naive()
if not naive(g, k): print("No K-Path")
