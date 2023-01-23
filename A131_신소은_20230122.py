# 백준
# 2108. 통계학

import sys
from collections import Counter
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

print(round(sum(nums)/N))
 
nums.sort()
print(nums[N//2])

cnt_nums = Counter(nums).most_common()
if len(cnt_nums) > 1 and cnt_nums[0][1]==cnt_nums[1][1]:
    print(cnt_nums[1][0])
else:
    print(cnt_nums[0][0])

print(max(nums)-min(nums))
