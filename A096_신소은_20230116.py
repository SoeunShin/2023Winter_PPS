# LeetCode
# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
    # str(n)으로 하면 통과되지 않음. count()에도 1이나 bin(1)이 아닌 '1'을 써야 통과됨 
