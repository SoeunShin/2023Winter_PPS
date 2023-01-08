# LeetCode
# 367. Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return math.sqrt(num) == math.ceil(math.sqrt(num))

# ceil이나 sqrt와 같은 math 모듈 안에 들어있는 함수를 사용할 때에는 import math를 해줘야 하는데
# LeetCode에서는 지원을 해주는건지 math를 import하지 않아도 실행이 된다.
