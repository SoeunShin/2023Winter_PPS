# LeetCode
# 342. Power of Four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (math.log(n,4) == round(math.log(n,4)))

# 로그로 변형하여 풀었다.
# 로그로 변형했을 때의 값이 자연수이면 true이므로, 반올림한 값이 원래의 값과 같은지 확인하였다.
# 또한 음수일 경우에는 무조건 false가 나오도록 하였다.
