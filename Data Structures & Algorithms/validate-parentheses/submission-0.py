class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return True
        bracket_stack = []

        bracket_pairs = { '}' : '{', ')': '(', ']': '['}
        
        for char in s:
            if char in bracket_pairs:
                if len(bracket_stack) > 0 and bracket_stack[-1] == bracket_pairs[char]:
                    bracket_stack.pop()
                else: 
                    return False
            else:
                bracket_stack.append(char)

        if len(bracket_stack) == 0:
            return True
        else:
            return False
        