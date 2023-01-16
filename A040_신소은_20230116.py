# LeetCode
# 1704. Determine if String Halves Are Alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']

        half = len(s)//2

        a = s.lower()[:half]
        b = s.lower()[half:]

        a_cnt = 0
        b_cnt = 0
        for i in range(half):
            if a[i] in vowels:
                a_cnt += 1
            if b[i] in vowels:
                b_cnt += 1

        return a_cnt == b_cnt
