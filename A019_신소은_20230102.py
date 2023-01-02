# 백준
# 2577. 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

mul = A*B*C

dic = {n:0 for n in range(10)}
for n in str(mul):
    dic[int(n)] += 1
for n in list(dic.values()):
    print(n)
