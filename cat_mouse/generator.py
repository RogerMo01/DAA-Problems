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
        axis[full[i]-1].append(full[i-1])
        axis[full[i-1]-1].append(full[i])

    for i in range(len(axis)):
        if len(axis[i]) == (len(nodes) - 1): full.remove(i+1)

    for i in range(M - len(axis) + 1):
        ind = choice(full)
        possible = [n for n in nodes if n not in axis[ind-1] and n != ind]
        ind2 = choice(possible)
        axis[ind-1].append(ind2)
        axis[ind2-1].append(ind)
        if len(axis[ind2-1]) == (len(nodes) - 1): full.remove(ind2)
        if len(possible) == 1: full.remove(ind)

    return axis

def gen_case(N, M):
    nodes = [i for i in range(1, N+1)]
    axis = gen_axis(nodes, M)
    
    return nodes, axis


def gen_graphs(count, lenght=3):
    examples = []
    
    for _ in range(count):
        N = randint(3, lenght)
        M = randint(N - 1, (N * (N-1) // 2))
        print(f'N:{N}, M:{M}')

        nodes, adj = gen_case(N, M)

        nodes = [x-1 for x in nodes]
        adj = [[y-1 for y in x] for x in adj]

        example_dict = {}
        for i in nodes: example_dict[i] = adj[i]

        examples.append(example_dict)

    return [Graph(x) for x in examples]



############################## GENERATE TEST CASES ################################
naive = DynamicSolution()

cases_qtty = 1
vertex_qtty = 50

graphs = gen_graphs(cases_qtty, vertex_qtty)
solutions = [naive(g) for g in graphs]

for i in range(len(solutions)):
    key = hash(str(datetime.datetime.now()))
    dictionary = {"graph": graphs[i].adj, "solution": solutions[i]}
    with open(f'cat_mouse/tests/test{key}.json', 'w') as file:
        string = json.dumps(dictionary)
        file.write(string)
###################################################################################
