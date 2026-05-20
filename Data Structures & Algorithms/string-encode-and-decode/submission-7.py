class Solution:

    def encode(self, strs: List[str]) -> str:
        deli = "#"
        ans = ""
        for st in strs:
            length = len(st)
            ans += str(length) + deli + st
        return ans

    def decode(self, s: str) -> List[str]:
        # where is the start of the words?
        # how many characters the words has?

        #   st
        # 5#Hello5#World
        #        en

        st = 0
        ans = []
        while st < len(s) :
            en = st
            while s[en] != "#":
                en += 1
            length = int(s[st:en])
            st = en + 1
            en = st + length

            ans.append(s[st:en])
            st = en
        return ans

            


          
