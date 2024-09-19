import os
import json
import time
from dynamic_solution import DynamicSolution
from best_solution import BestSolution

path = 'cat_mouse/tests/'
test_cases = os.listdir(path)

solver = DynamicSolution()
# solver = BestSolution()

lap = 0
times = []
for _ in range(500):
    start = time.time()
    for case_name in test_cases:
        graph = {}
        solution = -2

        with open(path+case_name, 'r') as file:
            case = json.load(file)

            graph = case['graph'] 
            solution = case['solution']

            # Map string keys to integers
            for i in range(len(graph.items())):
                graph[i] = graph[f"{i}"]
                del graph[f"{i}"]

        solver_solution = solver(graph)

    lap+=1
    end = time.time()
    times.append(end-start)

    print(f"Lap: {lap}")

print(sum(times)/len(times))