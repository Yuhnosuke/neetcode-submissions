class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t, t_to_s = {}, {}

        for i in range(len(s)):
            if s[i] not in s_to_t:
                s_to_t[s[i]] = i
            
            if t[i] not in t_to_s:
                t_to_s[t[i]] = i
            
            if s_to_t[s[i]] != t_to_s[t[i]]:
                return False
        
        return True