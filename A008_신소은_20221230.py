# 1. 입력받은 숫자들을 list에 저장하기
# 2. if - 숫자 리스트와 오름차순으로 정렬된 리스트가 동일하면 ascending 출력
# 3. elif - 숫자 리스트와 내림차순으로 정렬된 리스트가 동일하면 descending 출력
# 4. else - 둘 다 아니면 mixed 출력 

num_list = list(map(int, input().split()))

if num_list == sorted(num_list):
    print("ascending")
elif num_list == list(reversed(sorted(num_list))):
    print("descending")
else:
    print("mixed")
