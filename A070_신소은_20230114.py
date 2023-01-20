# 백준
# 2164. 카드2

import sys # 시간을 줄이기 위해 
from collections import deque

cards = deque([n for n in range(1, int(sys.stdin.readline())+1)])

for i in list(cards):
    while(len(cards) > 1):
        cards.popleft()
        sec = cards.popleft()
        cards.append(sec)
print(cards[0])
