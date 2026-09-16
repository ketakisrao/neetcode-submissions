class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        word_dict = {"": True}
        for word in wordDict:
            word_dict[word] = True

        for i in range(0, len(s)):
            for j in range(i + 1, len(s) + 1):
                if dp[i] and s[i:j] in word_dict:
                    dp[j] = True

        return dp[len(s)]
