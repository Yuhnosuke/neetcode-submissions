class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromic_substrings = []

        def is_valid(left, right):
            return 0 <= left and right < len(s)
        
        def is_palindrome(left, right):
            return s[left] == s[right]

        def expand_from_center(left, right):
            while is_valid(left, right) and is_palindrome(left, right):
                palindromic_substrings.append(s[left:right+1])
                
                left -= 1
                right += 1


        for i in range(len(s)):
            expand_from_center(i, i)
            expand_from_center(i, i + 1)

        return len(palindromic_substrings)
