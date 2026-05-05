from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequency_map = defaultdict(int)

        for ch in s1:
            frequency_map[ch] += 1
            
        left = 0
        for right in range(0, len(s2)):
            if s2[right] in frequency_map:
                frequency_map[s2[right]] -= 1
            
            while (right - left + 1) > len(s1):
                if s2[left] in frequency_map:
                    frequency_map[s2[left]] += 1
                left += 1

            if all(value == 0 for value in frequency_map.values()):
                return True
        
        return False
            
        
