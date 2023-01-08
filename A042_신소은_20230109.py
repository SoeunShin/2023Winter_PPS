# LeetCode
# 844. Backspace String Compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        for i in s:
            if i == '#' and s.index('#') == 0:
                s = s[1:]
            elif i == '#' and s.index('#') != 0:
                s = s[:s.index('#')-1] + s[s.index('#')+1:]

            for i in t:
                if i == '#' and t.index('#') == 0:
                    t = t[1:]
                elif i == '#' and t.index('#') != 0:
                    t = t[:t.index('#')-1] + t[t.index('#')+1:] 
        return s==t
