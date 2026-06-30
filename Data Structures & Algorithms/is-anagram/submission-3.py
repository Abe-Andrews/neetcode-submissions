class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        string_1_map = {}
        for letter in s:
            if letter in string_1_map:
                string_1_map[letter] += 1
            else:
                string_1_map[letter] = 1

        string_2_map = {}
        for letter in t:
            if letter in string_2_map:
                string_2_map[letter] += 1
            else:
                string_2_map[letter] = 1        

        for letter, count in string_1_map.items():
            map_2_count = string_2_map.get(letter)

            if count != map_2_count:
                return False

        return True
   

        