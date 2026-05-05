class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch_to_freq = {}
        for i in range(len(s)):
            ch = s[i]
            if ch not in ch_to_freq:
                ch_to_freq[ch] = 0
            ch_to_freq[ch] += 1
        
        for i in range(len(t)):
            ch = t[i]
            if ch not in ch_to_freq:
                return False
            ch_to_freq[ch] -= 1
        
        return not any(ch_to_freq.values())
            