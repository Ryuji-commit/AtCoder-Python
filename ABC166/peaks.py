n, m = map(int, input().split())
h_list = list(map(int, input().split()))
loads = [[0] for i in range(n)]
count = 0
for k in range(m):
    start, end = map(int, input().split())
    loads[start-1].append(h_list[end-1])
    loads[end-1].append(h_list[start-1])

for k in range(n):
    if h_list[k] > max(loads[k]):
        count += 1

print(count)
