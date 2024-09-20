from typing import Any
from itertools import permutations, combinations

class Naive:
    def __init__(self):
        self.char_counter = None

    def __call__(self, s: str, k: int):
        """Calculates the response"""

        self.char_counter = self.get_frequency_characters_string(s)

        if len(s) == 1: return s

        if not self.valid_start(k): return -1
        
        # Generate 2-combinations  
        char_combinations_list = []
        for x in combinations(set(s), 2):
            char_combinations_list.append(x)
        
        # Generate string permutations
        permutations = self.generate_permutations(s)

        # Take minor good string
        best = None
        for item in permutations:
            if self.is_good_strings(item, char_combinations_list, k):
                if best:
                    best = item if item < best else best
                else:
                    best = item 

        return best if best else -1


    def get_frequency_characters_string(self, s):
        char_counter = {}
        for char in s:
            if char in char_counter:
                char_counter[char] += 1
            else:
                char_counter[char] = 1
        
        return char_counter


    def valid_start(self, k):
        max_frequency = max(self.char_counter.values())
        min_frequency = min(self.char_counter.values())

        if max_frequency - min_frequency > k: 
            return False
        
        return True
    

    def generate_permutations(self, s):
        perms = permutations(s)
        return [''.join(p) for p in perms]


    def is_good_strings(self, string: str, char_combinations_list: list[tuple[str, str]], k: int):
        frequency_suffix = {}

        for i in range(len(string) - 1, -1, -1):
            char = string[i]
            if char in frequency_suffix:
                frequency_suffix[char] += 1
            else:
                frequency_suffix[char] = 1

            for item in char_combinations_list:
                x = item[0]
                y = item[1]
                if x in frequency_suffix:
                    if y in frequency_suffix:
                        if abs(frequency_suffix[x] - frequency_suffix[y]) > k:
                            return False
                    else:
                        if frequency_suffix[x] > k:
                            return False
                else:
                    if y in frequency_suffix:
                        if frequency_suffix[y] > k:
                            return False
            
        return True