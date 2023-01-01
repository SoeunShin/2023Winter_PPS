# programmers
# 문자열 다루기 기본

# 1. s의 길이가 4 혹은 6이고, s가 digit인지 아닌지 리턴

def solution(s):
    return (len(s)==4 or len(s)==6) and s.isdigit()
