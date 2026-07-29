class Solution:

    def is_palindrome(self, phrase, l, r):
        while l < r:
            if phrase[l] != phrase[r]:
                return False;
            l += 1
            r -= 1
        return True


    def partition(self, s: str) -> List[List[str]]:

        res = []
        curr = []
        
        def backtrack(start: int) -> None:
            if start == len(s):
                res.append(curr.copy())
                return
            
            for end in range(start, len(s)):
                if self.is_palindrome(s, start, end):
                    curr.append(s[start:end+1])
                    backtrack(end + 1)
                    curr.pop()
        
        backtrack(0)
        return res
    
    
    