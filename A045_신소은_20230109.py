# 백준
# 1157. 단어 공부

word = input().lower()
word_list = list(set(word)) # set으로 중복된 값을 제거해준 후 다시 list로 변형

cnt = [] # 각 글자의 개수를 저장할 list 
for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2: # max값이 2개 이상이면 "?" 출력
    print("?")
else: # cnt list의 max값과 동일한 index에 있는 word_list의 알파벳을 대문자로 출력
    print(word_list[(cnt.index(max(cnt)))].upper())
