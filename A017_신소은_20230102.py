# 백준
# 1475. 방 번호

# 1. 각 자리의 숫자들로 dic을 만듦
# 2. 각 숫자들의 개수를 dic에 저장
# 3. 6과 9의 개수를 더하고 2로 나눈 숫자(올림)와 나머지 개수들 중 가장 큰 수를 비교

import math

num = input() # str type
dic = {n:0 for n in range(10)}

for n in num:
    if n == '6' or n == '9':
        if dic[6] < dic[9]: # dic의 key로는 int type을 사용해야 에러가 나지 않는다. 왜지??
            dic[6] += 1
        else: dic[9] += 1
    else: dic[int(n)] += 1
print(max(dic.values()))
