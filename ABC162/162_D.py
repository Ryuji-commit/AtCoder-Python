N = int(input())
S = list(input())

# RGBとなる組み合わせの数を求める
sum_collection = S.count('R') * S.count('G') * S.count('B')

# RGBとなる組み合わせの数から、 j - i == k - jとなる組の数を減らす
for i in range(N):
    for j in range(i, N):
        # j - i == k - j　となる組を見つける
        k = j + (j - i)
        if k >= N:
            break
        # すべて違ったら　(R G Bの組み合わせであったら)
        if S[i] != S[j] != S[k] != S[i]:
            sum_collection -= 1

print(sum_collection)


