# programmers
# 나누어 떨어지는 숫자 배열

# 1. arr를 오름차순으로 sort
# 2. 배열의 개수만큼 반복
#   2-1. divisor로 나눠떨어지는 숫자이면
#       2-1-1. result 배열에 append
# 3. result 배열의 길이가 0이면 result 배열에 -1을 append

def solution(arr, divisor):
    result = []
    for num in sorted(arr):
        if num % divisor == 0:
            result.append(num)
    if len(result) == 0:
        result.append(-1)
    return result
