from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        appearance_map = defaultdict(int)
        left = 0
        answer = 0
        max_f = 0
        for right in range(0, len(s)):
            appearance_map[s[right]] += 1

            while (right - left + 1) - max(appearance_map.values()) > k:
                appearance_map[s[left]] -= 1
                left += 1 
            answer = max(answer, right - left + 1)
        return answer