# 백준
# 10867. 중복 빼고 정렬하기

_ = input()

# 숫자를 입력받아 int list로 만든 다음 set으로 중복을 제거하고, sort를 한 후 다시 list로 변환 
n_list = list(set(list(map(int, input().split()))))
n_list.sort()
n_list = list(map(str, n_list)) # str list로 변환 

# 숫자를 하나씩 출력
for i in n_list:
    print(i, end=' ') # 숫자 사이에 엔터 대신 ' '가 들어가도록
    
#print(' '.join(n_list))을 사용하면 왜 틀렸다고 나오는지 모르겠음
