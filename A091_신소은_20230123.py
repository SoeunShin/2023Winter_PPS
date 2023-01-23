# LeetCode
# 27. Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val):
            nums.remove(val)
        return len(nums)
