N, M = map(int, input().split())
A = list(map(int, input().split()))

holiday = N - sum(A)
print(holiday if holiday >= 0 else -1)
