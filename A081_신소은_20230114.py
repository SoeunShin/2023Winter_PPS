# 백준
# 2693. N번째 큰 수

n = int(input())

for i in range(n):
    n_list = sorted(list(map(int, input().split())), reverse=True) # 내림차순 저장
    print(n_list[2]) # index 2의 숫자 출력 
