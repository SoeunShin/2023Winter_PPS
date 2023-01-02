# LeetCode
# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {n:0 for n in nums}

        for n in nums:
            dic[n] += 1

        for n in dic.items():
            if n[1] == 1:
                return n[0]

# 아래 방법은 시간 복잡도가 큼
#        for n in nums:
#            if nums.count(n) == 1:
#                return n
