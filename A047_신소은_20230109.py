# 백준
# 11721. 열 개씩 끊어 출력하기

word = input()
for i in range(0, len(word), 10): # word의 길이에서 10씩 건너뜀
    print(word[i:i+10]) # 현재 index부터 10개의 글자를 출력
