N, K = map(int, input().split())
first_num = N % K
second_num = abs(first_num - K)
print(min(first_num, second_num))

