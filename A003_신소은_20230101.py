# LeetCode
# 66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # join을 사용하기 위해 int 리스트를 str 리스트로 바꿔준 후 다시 int로 만들어 1을 더해줌 
        num = int(''.join(list(map(str, digits))))+1
        # list로 만들기 위해 num을 str로 바꿔준 후 다시 int 리스트로 변형
        return list(map(int, list(str(num))))
