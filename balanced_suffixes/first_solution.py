from naive import Naive

class FirstSolution(Naive):
    def __call__(self, s: str, k: int):
        
        self.char_counter = self.get_frequency_characters_string(s)
        
        char_combinations_list = self.get_char_combination_list()

        if len(s) == 1: return s
        
        if(k == 0 and len(self.char_counter) != 1): return -1

        # frequency counter of characters sorted in descending order O(nlogn)
        character_sorted_desc = dict(sorted(self.char_counter.items(), key=lambda x: x[0], reverse=True))

        # frequency counter in the chain under construction
        character_frequency = dict.fromkeys(character_sorted_desc.keys(), 0)

        result = ''

        flag_add = True

        while (flag_add and len(character_sorted_desc) != 0):
            flag_break = False

            char = next(iter(character_sorted_desc))
            character_sorted_desc[char] -= 1
            character_frequency[char] += 1

            frequency_char = character_frequency[char]

            for other_char in char_combinations_list[char]:
                frequency_other = character_frequency[other_char]

                if abs(frequency_char - frequency_other) <= k:
                    continue

                else:
                    if other_char in character_sorted_desc:
                        character_sorted_desc[char] += 1
                        character_frequency[char] -= 1
                        result += other_char
                        character_sorted_desc[other_char] -= 1
                        character_frequency[other_char] += 1
                        if character_sorted_desc[other_char] == 0: del character_sorted_desc[other_char]
                        flag_add = True
                        flag_break = True
                        break

                    else:
                        flag_add = False
                        flag_break = True
                        continue
            
            if not flag_break: 
                result += char
                if character_sorted_desc[char] == 0: del character_sorted_desc[char]
                flag_add = True


        if len(character_sorted_desc) != 0:
            return -1

        elif len(character_sorted_desc) == 0:
            # result = ''.join(result)
            reversed_string = result[::-1]
            return reversed_string
        

    def get_char_combination_list(self):
        char_combinations_list = {}
        for item1 in self.char_counter.keys():
            characters = []
            for item2 in self.char_counter.keys():
                if item1 != item2:
                    characters.append(item2)

            char_combinations_list[item1] = sorted(characters,reverse=True)

        return char_combinations_list