# 백준
# 9546. 3000번 버스

n = int(input())

for _ in range(n):
    k = int(input())
    p = 1
    for _ in range(k-1):
        p  = p*2+1
    print(p)
