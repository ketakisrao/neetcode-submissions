class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s is None and t is None:
            return True
        if len(s) != len(t):
            return False
        if s is None or t is None:
            return False
        char_dict = {}


        for char in s:
            char = char.lower()
            if char.isalpha() and char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        for char in t:
            char = char.lower()
            if char.isalpha() and char in char_dict and char_dict[char] > 0:
                char_dict[char] -= 1
            else:
                return False
        return True

        