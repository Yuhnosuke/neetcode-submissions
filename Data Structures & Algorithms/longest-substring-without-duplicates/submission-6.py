class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ans = 0

        for r in range(len(s)):
            while s[r] in s[l:r]:
                l += 1
            ans = max(ans, r - l + 1)
        return ans