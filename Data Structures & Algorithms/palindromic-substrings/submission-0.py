class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        for i, char in enumerate(s):
            temp_i = i
            j = i
            while i < len(s) and i >=0 and j < len(s) and j >= 0 and s[i] == s[j]:
                counter += 1
                i -= 1
                j += 1
            i = temp_i
            j = temp_i + 1
            while i < len(s) and i >=0 and j < len(s) and j >= 0 and s[i] == s[j]:
                counter += 1
                i -= 1
                j += 1

        return counter
        