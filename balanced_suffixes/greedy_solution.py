from naive import Naive

class GreedySolution(Naive):
    def __call__(self, s: str, k: int):

        self.char_counter = self.get_frequency_characters_string(s)

        if not self.valid_start(k): return -1

        if(k == 0 and len(self.char_counter) != 1): return -1
        
        # frequency counter of characters sorted in descending order O(nlogn)
        character_sorted = dict(sorted(self.char_counter.items(), key=lambda x: x[0]))
    
        result = []

        while len(result) < len(s):
            for char in character_sorted:
                if self.char_counter[char] == 0:
                    continue
                
                self.char_counter[char] -= 1
                max_frequency = max(self.char_counter.values())
                min_frequency = min([frequency for frequency in self.char_counter.values()])

                if max_frequency - min_frequency <= k:
                    result.append(char)
                    break
                else:
                    self.char_counter[char] += 1

        return ''.join(result)
