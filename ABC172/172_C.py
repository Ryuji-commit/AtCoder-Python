N, M, K = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

a = [0]
b = [0]

# Aの机だけを上から読んでいく時のそれぞれの読了時間(Bは考慮しない)
for i in range(N):
    a.append(a[i] + A_list[i])
# 同じくBの読了時間
for i in range(M):
    b.append(b[i] + B_list[i])

ans, j = 0, M
# Aの机にある本を読まない場合からスタート
for i in range(N + 1):
    if a[i] > K:
        break
    # Kに収まるようにjを上から見ていく(単調増加)
    while b[j] + a[i] > K:
        j -= 1
    # 条件を満たすうち、最大なものを求める
    ans = max(ans, i + j)

print(ans)
