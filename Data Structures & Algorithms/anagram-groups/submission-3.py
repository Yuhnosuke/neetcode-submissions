class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_to_words = defaultdict(list)

        for s in strs:
            f = [0] * 26

            for ch in s:
                i = ord(ch) - ord("a")
                f[i] +=1
            
            freq_to_words[tuple(f)].append(s)
        
        return list(freq_to_words.values())
            

