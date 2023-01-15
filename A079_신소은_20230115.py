# programmers
# K 번째 수

"""
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
"""

def solution(array, commands):
    ans = []
    for i in range(len(commands)):
        start = commands[i][0]
        finish = commands[i][1]
        idx = commands[i][2]
        # index는 0부터 시작하므로 1을 빼줘야 함 : 뒤에 있는 숫자는 어차피 포함되지 않으므로 finish에서 1을 뺄 필요 없음 
        sort_list = sorted(array[start-1:finish]) 
        ans.append(sort_list[idx-1]) # # index는 0부터 시작하므로 1을 빼줘야 함
    return ans
