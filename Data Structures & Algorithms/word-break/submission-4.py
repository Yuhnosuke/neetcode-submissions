class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dp(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            memo[i] = False
            for word in wordDict:
                if s.startswith(word, i):
                    if dp(i + len(word)):
                        memo[i] = True
                        return True
            return memo[i]
        
        memo = {}
        return dp(0)