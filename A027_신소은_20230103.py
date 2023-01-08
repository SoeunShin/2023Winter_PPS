# 백준
# 2953. 나는 요리사다

max_n = 0
max_cnt = 0
for i in range(5):
    n_sum = sum(list(map(int, input().split())))
    if max_n < n_sum:
        max_n = n_sum
        max_cnt = i+1
print(max_cnt, max_n)
