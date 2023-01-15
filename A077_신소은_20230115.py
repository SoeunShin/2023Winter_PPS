# 백준
# 2822. 점수 계산

n_list = [] # 모든 점수 저장
idx_list = [] # 가장 큰 숫자 5개의 번호를 저장
for i in range(8):
    n_list.append(int(input()))

sort_list = list(reversed(sorted(n_list))) # 점수를 큰 순서대로 배열 
print(sum(sort_list[:5])) # 가장 큰 숫자 5개의 합 출력 

idx_list = [n_list.index(n)+1 for n in sort_list[:5]] # 몇 번째 점수였는지 저장

idx_list = list(map(str, sorted(idx_list))) # 오름차순 정렬 후 str list로 변환 
print(' '.join(idx_list)) # 숫자 사이에 빈칸을 넣고 str 타입으로 출력 
