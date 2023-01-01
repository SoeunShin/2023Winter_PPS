# 백준
# 4344. 평균은 넘겠지

# 1. 줄 수를 입력받아 저장
# 2. 입력받은 줄 수만큼 반복
#   2-1. 한 줄로 입력받은 숫자들을 리스트로 저장
#   2-2. 한 줄의 평균을 구하여 저장
#       2-2-1. 그 줄의 개수만큼 반복
#       2-2-2. 그 줄에서 평균보다 높은 점수의 개수 카운트
#   2-4. 비율을 계산하고 소숫점 셋째자리에서 반올림하여 출력

num = int(input())

for i in range(num):
    num_list = list(map(int, input().split()))
    avg = (sum(num_list)-num_list[0])/num_list[0]
    cnt = 0
    for j in range(num_list[0]):
        if num_list[j+1] > avg:
            cnt += 1
    print(format(round(cnt/num_list[0]*100, 3), '0.3f'), '%', sep='')
