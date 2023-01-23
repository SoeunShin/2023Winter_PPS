# 백준
# 1292. 쉽게 푸는 문제

A, B = map(int, input().split())
num = [0]

for i in range(46):
    for j in range(i):
        num.append(i)

print(sum(num[A:B+1]))
