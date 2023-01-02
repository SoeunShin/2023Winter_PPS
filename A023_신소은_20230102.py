# LeetCode
# 258. Add Digits

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            n_list = list(map(int, str(num)))
            num = int(sum(n_list))
        return num
