# LeetCode
# 728. Self Dividing Numbers

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = [num for num in range(left,right+1) if '0' not in str(num)]
        answer = [num for num in answer if 0 not in [num % int(n) == 0 for n in str(num)]]
        return answer
