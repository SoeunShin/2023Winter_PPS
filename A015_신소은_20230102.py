# 백준
# 2475. 검증수

num_list = list(map(int, input().split()))
print(sum(n**2 for n in num_list)%10)
