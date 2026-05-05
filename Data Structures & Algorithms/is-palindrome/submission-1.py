class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = ""

        for ch in s:
            if ch.isalnum() and ch != " ":
                processed += ch.lower()
        
        l, r = 0, len(processed) - 1
        while l < r:
            if processed[l] != processed[r]:
                return False
            l += 1
            r -= 1
        return True