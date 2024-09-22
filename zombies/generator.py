import json
import datetime
from graph import Graph
from naive import Naive
from random import randint, shuffle, choice
import sys

sys.setrecursionlimit(10**6)

def gen_axis(nodes, M):
    axis = [[] for _ in range(len(nodes))]

    pairs = []
    for u in nodes:
        for v in nodes:
            if u < v: pairs.append((u, v))

    for _ in range(M):
        max = len(pairs)-1
        i = randint(0, max)
        u, v = pairs[i]

        axis[u].append(v)
        axis[v].append(u)

        del pairs[i]

    return axis
        


def gen_graph(N, M):
    nodes = [i for i in range(0, N)]
    axis = gen_axis(nodes, M)
    return nodes, axis


def gen_graphs(count, max_lenght):
    for _ in range(count):
        N = randint(10, max_lenght)
        M = randint(0, (N*(N-1))//2)
        print(f'N:{N}')
        print(f'M:{M}')

        nodes, adj = gen_graph(N, M)

        example_dict = {}
        for i in nodes: example_dict[i] = adj[i]

        yield Graph(example_dict)



############################## GENERATE TEST CASES ################################
naive = Naive()

cases_qtty = 1
vertex_max_qtty = 11

counter = 1
for graph in gen_graphs(cases_qtty, vertex_max_qtty):

    k = randint(0, len(graph))
    print(f'K:{k}')

    solution = 1 if naive(graph, k) else 0

    key = hash(str(datetime.datetime.now()))
    dictionary = {"graph": graph.adj, "k": k, "solution": solution}
    with open(f'zombies/tests/test{key}.json', 'w') as file:
        string = json.dumps(dictionary)
        file.write(string)

    print(f"✔ Case {counter} generated")
    counter+=1
###################################################################################