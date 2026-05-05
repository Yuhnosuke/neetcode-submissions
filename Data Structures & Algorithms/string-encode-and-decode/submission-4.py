class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        separator = "#"

        for word in strs:
            length = len(word)
            encoded += f"{length}{separator}{word}"
        
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        start = 0
        separator = "#"
        ans = []

        while start < len(s):
            end = start

            while s[end] != separator:
                end += 1
            
            length = s[start:end]

            start = end + 1
            end = start + int(length)

            ans.append(s[start:end])

            start = end

        return ans

