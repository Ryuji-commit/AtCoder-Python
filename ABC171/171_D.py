import collections

N = int(input())
A_list = list(map(int, input().split()))
A_count_list = collections.Counter(A_list)
A_sum = sum(A_list)
Q = int(input())
for _ in range(Q):
    B, C = map(int, input().split())
    A_sum += (C - B)*A_count_list[B]
    A_count_list[C] += A_count_list[B]
    A_count_list[B] = 0
    print(A_sum)

