from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        answer = 0
        current_str = deque()

        for right in range(0, len(s)):
            while s[right] in current_str:
                current_str.popleft()
                left += 1
            current_str.append(s[right])
            
            answer = max(answer, len(current_str))
        
        return answer