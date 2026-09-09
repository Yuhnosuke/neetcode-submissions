class Solution:
    sep = "#"

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            length = str(len(string))
            encoded += length + self.sep + string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        st = 0

        while st < len(s):
            en = st
            
            while s[en] != self.sep:
                en += 1

            length = int(s[st:en])
            st = en + 1
            en = st + length
            decoded.append(s[st:en])
            st = en

        return decoded
