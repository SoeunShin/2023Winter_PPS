# 백준
# 18258. 큐2

import sys # 시간을 줄이기 위해 
from collections import deque

n = int(input())
q = deque()

for i in range(n):
    com = sys.stdin.readline().split() # 명령어를 list로 만듦 
    if com[0] == 'push':
        q.append(com[1])
    elif com[0] == 'pop':
        if q: # q가 비어있지 않으면 
            print(q.popleft()) # popleft는 가장 앞에있는 원소를 꺼냄 
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(q))
    elif com[0] == 'empty':
        if q: # q가 비어있지 않으면
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if q: # q가 비어있지 않으면
            print(q[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if q: # q가 비어있지 않으면
            print(q[-1])
        else:
            print(-1)
