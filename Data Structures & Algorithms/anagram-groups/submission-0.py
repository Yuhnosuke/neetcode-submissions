from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        if len(strs) == 1:
            return [strs]
        
        anagram_map = defaultdict(list)
        for i in range(0, len(strs)):
            sorted_s = "".join(sorted(strs[i]))
            anagram_map[sorted_s].append(strs[i])

        answer = []
        for v in anagram_map.values():
            answer.append(v)
        return answer