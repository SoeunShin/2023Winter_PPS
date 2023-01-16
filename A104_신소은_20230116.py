# 백준
# 14487. 욱제는 효도쟁이야!!

_ = input()

n_list = list(map(int, input().split()))

n_list.sort()
print(sum(n_list[:len(n_list)-1]))
