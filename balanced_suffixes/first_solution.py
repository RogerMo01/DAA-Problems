from naive import Naive
from itertools import combinations

class FirstSolution(Naive):
    def __call__(self, s: str, k: int):
        
        self.char_counter = self.get_frequency_characters_string(s)
        
        if len(s) == 1: return s
        
        if(k == 0 and len(self.char_counter) != 1): return -1

        # frequency counter of characters sorted in descending order O(nlogn)
        character_sorted_desc = dict(sorted(self.char_counter.items(), key=lambda x: x[0], reverse=True))

        # frequency counter in the chain under construction
        character_frequency = dict.fromkeys(character_sorted_desc.keys(), 0)

        char_copy = sorted(self.char_counter.keys(), reverse=True) 

        # combinations for any pair of characters in the original string  O(n^2)
        char_combinations_list = []
        for char_i, char_j in combinations(char_copy, 2):
            char_combinations_list.append((char_i, char_j))

        result = []

        first_char = char_copy[0]
        character_sorted_desc[first_char] -= 1
        if character_sorted_desc[first_char] == 0: del character_sorted_desc[first_char]
        character_frequency[first_char] += 1
        result.append(first_char)

        flag_add = True

        while (flag_add and len(character_sorted_desc) != 0):
            flag_break = False

            char = next(iter(character_sorted_desc))
            character_sorted_desc[char] -= 1
            character_frequency[char] += 1

            for item in char_combinations_list:
                char_i = item[0]
                char_j = item[1]
                frequency_i = character_frequency[char_i]
                frequency_j = character_frequency[char_j]

                if abs(frequency_i - frequency_j) <= k:
                    continue

                else:
                    char_x = ''
                    if(char_i == char):
                        char_x = char_j
                    else: 
                        char_x == char_i

                    if char_x in character_sorted_desc:
                        character_sorted_desc[char] += 1
                        character_frequency[char] -= 1
                        result.append(char_x)
                        character_sorted_desc[char_x] -= 1
                        character_frequency[char_x] += 1
                        if character_sorted_desc[char_x] == 0: del character_sorted_desc[char_x]
                        flag_add = True
                        flag_break = True
                        break

                    else:
                        flag_add = False
                        flag_break = True
                        break
            
            if not flag_break: 
                result.append(char)
                if character_sorted_desc[char] == 0: del character_sorted_desc[char]
                flag_add = True


        if len(character_sorted_desc) != 0:
            return -1

        elif len(character_sorted_desc) == 0:
            result = ''.join(result)
            reversed_string = result[::-1]
            return reversed_string