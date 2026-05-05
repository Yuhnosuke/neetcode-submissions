class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        answer = 0

        for right in range(0, len(s)):
            while s[right] in s[left:right]:                
                left += 1
            answer = max(answer, right - left + 1)
        
        return answer