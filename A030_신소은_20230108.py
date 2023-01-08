# 백준
# 17211. 좋은 날 싫은 날

N, now = map(int, input().split())
GG, GB, BG, BB = map(float, input().split())

G_cnt = [0 for _ in range(N)]
B_cnt = [0 for _ in range(N)]

if now == 0: # 좋은 날
    G_cnt[0] = GG # 둘째 날에 좋은 날을 저장 
    B_cnt[0] = GB # 둘째 날에 싫은 날을 저장
else:
    G_cnt[0] = BG # 둘째 날에 좋은 날을 저장
    B_cnt[0] = BB # 둘째 날에 싫은 날을 저장

for i in range(1, N):
    G_cnt[i] = G_cnt[i-1]*GG + B_cnt[i-1]*BG
    B_cnt[i] = G_cnt[i-1]*GB + B_cnt[i-1]*BB

print(round(G_cnt[N-1]*1000))
print(round(B_cnt[N-1]*1000))
