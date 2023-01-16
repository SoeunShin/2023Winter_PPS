# 백준
# 3062. 수 뒤집기

n = int(input())

for i in range(n):
    num = input()
    s = int(num) + int(num[::-1]) # 원래 숫자와 뒤집은 숫자의 합 
    if str(s) == str(s)[::-1]: # 합한 숫자가 좌우대칭이면 
        print('YES')
    else:
        print('NO')
