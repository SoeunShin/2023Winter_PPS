# 백준
# 5355. 화성 수학

# @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자

n = int(input())

for _ in range(n):
    my_list = list(input().split())
    num = float(my_list.pop(0))
    for j in range(len(my_list)):
        if my_list[j] == '@':
            num *= 3
        elif my_list[j] == '%':
            num += 5
        else:
            num -= 7
    print(format(num, '.2f'))
