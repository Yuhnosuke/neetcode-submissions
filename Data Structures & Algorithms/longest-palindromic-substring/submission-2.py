class Solution:
    def longestPalindrome(self, s: str) -> str:           
        answer = ""

        def is_valid(left, right):
            return left >= 0 and right < len(s)
        
        def is_palindrome(left, right):
            return s[left] == s[right]

        for i in range(len(s)):

            left = i
            right = i

            while is_valid(left, right) and is_palindrome(left, right):
                current_palindrome = s[left:right+1]
                if len(current_palindrome) > len(answer):
                    answer = current_palindrome
                
                left -= 1
                right += 1
            
            left = i
            right = i + 1
            
            while is_valid(left, right) and is_palindrome(left, right):
                current_palindrome = s[left:right+1]
                if len(current_palindrome) > len(answer):
                    answer = current_palindrome
                
                left -= 1
                right += 1

        return answer
        