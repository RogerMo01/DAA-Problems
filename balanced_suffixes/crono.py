import os
import json
import time
from first_solution import FirstSolution
from second_solution import SecondSolution

path = 'balanced_suffixes/tests/'
test_cases = os.listdir(path)

# solver = FirstSolution()
solver = SecondSolution()

lap = 0
times = []
for _ in range(500):
    start = time.time()
    for case_name in test_cases:
        s = ''
        k = -1
        solution = -2

        with open(path+case_name, 'r') as file:
            case = json.load(file)

            s = case['string'] 
            k = case['k']
            solution = case['solution']

        solver_solution = solver(s, k)

    lap+=1
    end = time.time()
    times.append(end-start)

    print(f"Lap: {lap}")

print(sum(times)/len(times))