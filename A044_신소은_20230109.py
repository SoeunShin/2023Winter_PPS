# LeetCode
# 551. Student Attendance Record I

class Solution:
    def checkRecord(self, s: str) -> bool:
        late = 0
        fail = 0
        if s.count('A') < 2: # 결석 2번 미만 
            for i in s:
                if i == 'L': 
                    late += 1
                    if late == 3: # L 연속 3번 이상 
                        fail = 1 # fail
                else: late = 0 # 연속으로 나오지 않으면 초기화 
            if fail == 0:
                return True
        return False
