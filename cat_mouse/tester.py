import os
import json
from dynamic_solution import DynamicSolution
from naive import Naive
from best_solution import BestSolution

path = 'cat_mouse/tests/'
test_cases = os.listdir(path)

# solver = Naive()
# solver = DynamicSolution()
solver = BestSolution()

total_cases = len(test_cases)
print(f"{total_cases} Test cases")

case_i = 1
for case_name in test_cases:
    graph = {}
    solution = -2

    with open(path+case_name, 'r') as file:
        case = json.load(file)

        graph = case['graph'] 
        solution = case['solution']

        # Map string keys to integrs
        for i in range(len(graph.items())):
            graph[i] = graph[f"{i}"]
            del graph[f"{i}"]


    solver_solution = solver(graph)

    print(f"Case {case_i} of {total_cases}: {case_name}")
    print(f"🟢 {solver_solution}" if solver_solution == solution else f"🔴 {solver_solution}, but {solution} expected")
    case_i += 1
