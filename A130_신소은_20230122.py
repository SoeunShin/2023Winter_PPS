# 백준
# 10773. 제로

import sys # input()으로 받으면 3852ms, readline()으로 받으면 80ms 소요

K = int(sys.stdin.readline())
nums = []
for i in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        nums.pop()
    else:
        nums.append(n)
print(sum(nums))
