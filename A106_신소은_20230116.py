# 백준
# 3059. 등장하지 않는 문자의 합

n = int(input())
for i in range(n):
    sum_alpha = 2015 # 65~90까지의 합 
    s = set(list(input())) # 중복 제거 
    for ch in s:
        sum_alpha -= ord(ch)
    print(sum_alpha)
