import os
import json
from dynamic_solution import DynamicSolution

path = 'cat_mouse/tests/'
test_cases = os.listdir(path)

solver = DynamicSolution()

total_cases = len(test_cases)
print(f"{total_cases} Test cases")

for case_name in test_cases:
    case_i = 1
    graph = {}
    solution = -100

    with open(path+case_name, 'r') as file:
        content = file.read()
        case = json.loads(content)

        graph: dict = case['graph'] 
        solution = case['solution']

        # Map string keys to integrs
        for i in range(len(graph.items())):
            graph[i] = graph[f"{i}"]
            del graph[f"{i}"]

    solver_solution = solver(graph)

    print(f"Case {case_i} of {total_cases}: {case_name}")
    print(f"🟢 {solver_solution}" if solver_solution == solution else f"🔴 {solver_solution}, but {solution} expected")
