class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        s2_dict = {}
        
        for char in s1:
            if char in s1_dict:
                s1_dict[char] +=1
            else:
                s1_dict[char] = 1
        i = 0
        j = 0
        while j < len(s1) - 1:
            char = s2[j]
            if char in s2_dict:
                s2_dict[char] +=1
            else:
                s2_dict[char] = 1
            j += 1
        while j < len(s2):
            if s2[j] in s2_dict:
                s2_dict[s2[j]] +=1
            else:
                s2_dict[s2[j]] = 1

            if s1_dict == s2_dict:
                return True
            if s2_dict[s2[i]] > 1:
                s2_dict[s2[i]] -=1
            else:
                del s2_dict[s2[i]]
            i += 1
            j += 1
        return False
