# 백준
# 11650. 좌표 정렬하기

import sys
input = sys.stdin.readline # 실행 시간 줄이는 방법 

n = int(input())

arr = []
for i in range(n):
    [a, b] = map(int, input().split())
    arr.append([a, b])

s_arr = sorted(arr)

for i in range(n):
    print(s_arr[i][0], s_arr[i][1])
