# 백준
# 2941. 크로아티아 알파벳

word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    word = word.replace(i, '@')

print(len(word))
