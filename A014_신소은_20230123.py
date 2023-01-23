# LeetCode
# 228. Summary Ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = 0
        answer = []

        for i in range(len(nums)):
            if i+1<len(nums) and nums[i]+1 == nums[i+1]:
                continue
            if start == i:
                answer.append(str(nums[start]))
            else:
                answer.append(str(nums[start]) + "->" + str(nums[i]))

            start = i+1
        return answer
