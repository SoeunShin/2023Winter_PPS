# LeetCode
# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for n in nums:
            if nums.count(n) == 1:
                return n
