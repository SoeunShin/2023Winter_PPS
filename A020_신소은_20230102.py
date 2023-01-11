# 백준
# 2455. 지능형 기차

cnt = 0
cnt_list = []
for i in range(4):
    minus, plus = input().split()
    cnt -= int(minus)
    cnt_list.append(cnt)
    cnt += int(plus)
    cnt_list.append(cnt)

print(max(cnt_list))
