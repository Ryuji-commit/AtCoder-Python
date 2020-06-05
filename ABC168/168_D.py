N, M = map(int, input().split())
loads = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    loads[A-1].append(B-1)
    loads[B-1].append(A-1)

queue = [0]
dist = [0] * N
prev = [-1] * N
while(len(queue) != 0):
    now = queue[0]
    queue.pop(0)
    for i in loads[now]:
        if dist[i] != 0:
            continue
        else:
            queue.append(i)
            dist[i] = dist[now] + 1
            prev[i] = now + 1

print('Yes')
for i in prev[1:]:
    print(i)


