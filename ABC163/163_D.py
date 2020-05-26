N, K = map(int, input().split())
count = 0
mod = 10**9+7
for i in range(K, N+2):
    max_num = (i * (N + N - i + 1)) // 2
    min_num = (i * (i - 1)) // 2
    count += (max_num - min_num + 1)
    count %= mod

print(count)
