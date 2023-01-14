# 백준
# 1159. 농구 경기

num = int(input())
firstList = [] # 성을 저장할 list
five = ''
for i in range(num): # 선수의 수만큼 반복
    name = input()
    firstList.append(name[0]) # 성의 첫 글자만 list에 저장

unique = sorted(list(set(firstList))) # set으로 중복 이름을 제거한 후, 오름차순 list로 변형
for ch in unique: # 중복을 제거한 list의 각 알파벳을 순회
    if firstList.count(ch) >= 5: # 해당 알파벳의 개수가 5 이상이면
        five += ch

if five == '': # 성의 첫 글자가 같은 선수가 5명 이상인 성이 하나도 없다면
    print("PREDAJA")
else:
    print(five)
