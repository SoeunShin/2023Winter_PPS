# programmers
# 2016년

# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?

def solution(a, b):
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    num = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 윤년
    
    all = sum(num[:a-1]) + b
    return day[all%7] # 7로 나누어 떨어지는 날은 목요일이므로, day[0]을 목요일로 설정
