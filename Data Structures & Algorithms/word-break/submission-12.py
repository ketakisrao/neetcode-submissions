class Solution:
    def word_break(self, s: str, word_dict: dict, dp) -> bool:
        n = len(s)
        for i in range(0, n):
            for j in range(i + 1, n + 1):
                substr = s[i:j]
                if dp[i] and s[i:j] in word_dict:
                    dp[j] = True

        return dp[n]


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        word_dict = {"": True}
        for word in wordDict:
            word_dict[word] = True

        return self.word_break(s, word_dict, dp)
