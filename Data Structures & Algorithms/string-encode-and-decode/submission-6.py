class Solution:
    
    delimiter = "#"

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + self.delimiter + s
        
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        st = 0

        while st < len(s):
            en = st

            while s[en] != self.delimiter:
                en += 1
            
            length = int(s[st:en])

            st = en + 1
            en = st + length

            res.append(s[st:en])

            st = en
        
        return res
