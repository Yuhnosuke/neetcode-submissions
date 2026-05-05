class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordered_to_words = {}
        for word in strs:
            ordered = "".join(sorted(word))
            if ordered not in ordered_to_words:
                ordered_to_words[ordered] = []
            ordered_to_words[ordered].append(word)

        return list(ordered_to_words.values())
