class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = str(len(s))
            res += length + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        st = 0        
        res = []

        while st < len(s):
            en = st
            while s[en] != "#":
                en += 1
            length = int(s[st:en])
            st = en + 1
            en = st + length
            res.append(s[st:en])
            st = en
        return res



        
