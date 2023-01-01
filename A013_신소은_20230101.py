# LeetCode
# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for n in nums:
            if nums.count(n) == 1:
                return n

# 실행 시간이 너무 오래 걸린다... 다른 방법을 더 생각해볼 것!
