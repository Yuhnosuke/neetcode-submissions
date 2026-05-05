class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumerics = ""
        for i in range(0, len(s)):
            if s[i].isalnum():
                alphanumerics += s[i]
        lower_alphanumerics = alphanumerics.lower()

        left = 0
        right = len(lower_alphanumerics) - 1

        while left < right:
            if lower_alphanumerics[left] !=lower_alphanumerics[right]:
                return False
            left += 1
            right -= 1
        return True