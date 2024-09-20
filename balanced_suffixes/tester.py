import os
import json
from naive import Naive
from first_solution import FirstSolution
from greedy_solution import GreedySolution

path = 'balanced_suffixes/tests/'
test_cases = os.listdir(path)

# solver = Naive()
# solver = FirstSolution()
solver = GreedySolution()


total_cases = len(test_cases)
print(f"{total_cases} Test cases")

case_i = 1
for case_name in test_cases:
    string = ''
    k = -1
    solution = -2

    with open(path+case_name, 'r') as file:
        case = json.load(file)

        string = case['string'] 
        k = case['k']
        solution = case['solution']

    print(f"Case {case_i} of {total_cases}: {case_name}")
    solver_solution = solver(string, k)

    print(f"🟢 {solver_solution}" if solver_solution == solution else f"🔴 {solver_solution}, but {solution} expected")
    case_i += 1
