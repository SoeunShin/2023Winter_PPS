# LeetCode
# 169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique = list(set(nums))

        for n in unique:
            if nums.count(n) > len(nums)/2:
                return n
