# LeetCode
# 796. Rotate String

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        from collections import deque

        dq = deque(s)

        for i in range(len(s)):
            pop = dq.popleft()
            dq.append(pop)
            join = ''.join(dq)
            if join == goal:
                return True
        return False
