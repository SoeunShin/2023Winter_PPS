# LeetCode
# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ""

        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                alpha += s[i].lower()

        rev_list = list(reversed(list(alpha)))

        return ''.join(rev_list) == alpha
