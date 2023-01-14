# 백준
# 1316. 그룹 단어 체크

n = int(input())
cnt = n

for i in range(n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]: # word의 현재 글자가 다음 글자와 같으면 넘어감
            pass # 아무 수행도 하지 않길 원할 때 사용 
        elif word[j] in word[j+1:]: # word의 현재 글자와 다음 글자가 다른데, word의 뒷 부분에 현재 글자가 또 존재 (떨어져있다는 뜻)
            cnt -= 1 # 그룹 단어의 개수를 하나 줄임
            break
print(cnt)
            
            
