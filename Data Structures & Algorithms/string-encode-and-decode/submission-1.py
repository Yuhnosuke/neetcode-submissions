class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "#"

        res = ""

        for st in strs:
            length = len(st)
            encoded = str(length) + delimiter + st

            res += encoded
        
        return res

    def decode(self, s: str) -> List[str]:
        delimiter = "#"
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != delimiter:
                j += 1
            
            length = s[i : j]

            i = j + 1
            j = i + int(length)

            res.append(s[i : j])

            i = j

        return res

