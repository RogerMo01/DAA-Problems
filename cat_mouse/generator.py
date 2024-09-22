import json
import datetime
from graph import Graph
from naive import Naive
from dynamic_solution import DynamicSolution
from random import randint, shuffle, choice
import sys

sys.setrecursionlimit(10**6)

def gen_axis(nodes, M):
    axis = [[] for _ in range(len(nodes))]
    full = nodes.copy()
    shuffle(full)

    for i in range(1, len(full)):
        axis[full[i]].append(full[i-1])
        axis[full[i-1]].append(full[i])

    for i in range(len(axis)):
        if len(axis[i]) == (len(nodes) - 1): full.remove(i)

    for i in range(M - len(axis) + 1):
        ind = choice(full)
        possible = [n for n in nodes if n not in axis[ind] and n != ind]
        ind2 = choice(possible)
        axis[ind].append(ind2)
        axis[ind2].append(ind)
        if len(axis[ind2]) == (len(nodes) - 1): full.remove(ind2)
        if len(possible) == 1: full.remove(ind)

    return axis


def gen_graph(N, M):
    nodes = [i for i in range(0, N)]
    axis = gen_axis(nodes, M)
    return nodes, axis


def gen_graphs(count, lenght=3):
    for _ in range(count):
        N = randint(3, lenght)
        M = randint(N - 1, (N * (N-1) // 2))
        print(f'N:{N}, M:{M}')

        nodes, adj = gen_graph(N, M)

        example_dict = {}
        for i in nodes: example_dict[i] = adj[i]

        yield Graph(example_dict)



############################## GENERATE TEST CASES ################################
naive = Naive()

cases_qtty = 2
vertex_max_qtty = 10

counter = 1
for graph in gen_graphs(cases_qtty, vertex_max_qtty):
    solution = naive(graph)

    key = hash(str(datetime.datetime.now()))
    dictionary = {"graph": graph.adj, "solution": solution}
    with open(f'cat_mouse/tests/test{key}.json', 'w') as file:
        string = json.dumps(dictionary)
        file.write(string)

    print(f"✔ Case {counter} generated")
    counter+=1
###################################################################################
