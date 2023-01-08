# 백준
# 3052. 나머지

n_list = []
for i in range(10):
    n_list.append(int(input())%42)
print(len(set(n_list))) # set은 중복을 허용하지 않기 때문에 중복된 값을 제거함 
