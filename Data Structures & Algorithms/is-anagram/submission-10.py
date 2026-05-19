class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ch_to_freq = defaultdict(int)
        for sch in s:
            s_ch_to_freq[sch] += 1

        for tch in t:
            if tch not in s_ch_to_freq:
                return False
            s_ch_to_freq[tch] -= 1
        
        return not any(s_ch_to_freq.values())
            