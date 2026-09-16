decodings = {
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
    "6": "F",
    "7": "G",
    "8": "H",
    "9": "I",
    "10": "J",
    "11": "K",
    "12": "L",
    "13": "M",
    "14": "N",
    "15": "O",
    "16": "P",
    "17": "Q",
    "18": "R",
    "19": "S",
    "20": "T",
    "21": "U",
    "22": "V",
    "23": "W",
    "24": "X",
    "25": "Y",
    "26": "Z",
}
dp = {}
class Solution:
    def numDecodings(self, s: str) -> int:
        if s in dp:
            return dp[s]
        if s == "":
            return 1

        encoding1 = s[0:1]
        encoding2 = ""
        if len(s) >=2:
            encoding2 = s[0:2]
        sum1, sum2 = 0, 0
        left = s[1:]
        right = s[2:]
        if encoding1 in decodings:
            sum1 = self.numDecodings(left)
            
        if encoding2 in decodings:
            sum2 = self.numDecodings(right)

        dp[s] = sum1 + sum2
        return sum1 + sum2
        

        
       
            