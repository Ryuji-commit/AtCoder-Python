N, K = map(int, input().split())
A = list(i - 1 for i in map(int, input().split()))
now = 0
loop_start = 0
load_list = [-1] * N
Y = - 1
while loop_start < K:
    if load_list[now] == -1:
        load_list[now] = loop_start
        now = A[now]
        loop_start += 1
    else:
        start = load_list[now]
        end = loop_start - load_list[now]
        Y = start + (K - loop_start) % end
        break

if Y == -1:
    print(now + 1)
else:
    print(load_list.index(Y) + 1)



