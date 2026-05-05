from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        appearance_map = defaultdict(int)
        for ch in s:
            appearance_map[ch] += 1
        
        for ch in t:
            if ch not in appearance_map:
                return False
            appearance_map[ch] -= 1

        return all(v == 0 for v in appearance_map.values())