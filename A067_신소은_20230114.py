# LeetCode
# 1047. Remove All Adjacent Duplicates In String

class Solution:
    def removeDuplicates(self, s: str) -> str:
        final = list()
        for ch in s:
            # if final은 final이 비어있지 않으면 실행됨
            if final and final[-1] == ch: # final이 비어있지 않고, final의 마지막 글자가 현재 글자와 같으면 (결국 중복될 것이기 때문)
                final.pop() # final의 가장 마지막 원소를 제거 
            else:
                final.append(ch) # final에 현재 글자를 추가
        return "".join(final)
