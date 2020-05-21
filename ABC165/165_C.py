import itertools

N, M, Q = map(int, input().split())
input_lists = []
A = []
point = [0]

for _ in range(Q):
    input_lists.append([int(i) for i in input().split()])

for A in itertools.combinations_with_replacement(range(1, M+1), N):
    d_sum = 0
    for input_list in input_lists:
        a, b, c, d = input_list
        if A[b-1] - A[a-1] == c:
            d_sum += d
    point.append(d_sum)

print(max(point))
