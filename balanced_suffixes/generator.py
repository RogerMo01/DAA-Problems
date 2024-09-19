import json
import random
import datetime
from naive import Naive

def gen_case(min, max, alphabeth):

    string_len = random.randint(min, max)
    string = ''.join(random.choices(alphabeth, k=string_len))
    k = random.randint(0, 4)

    return string, k

############################## GENERATE TEST CASES ################################
naive = Naive()

alphabeths = [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd', 'e']]

for alphabeth in alphabeths:
    for _ in range(200):
        s, k = gen_case(5, 10, alphabeth)
        solution = naive(s, k)
        
        key = hash(str(datetime.datetime.now()))
        dictionary = {"string": s, "k": k, "solution": solution}
        with open(f'balanced_suffixes/tests/test{key}.json', 'w') as file:
            string = json.dumps(dictionary)
            file.write(string)
###################################################################################