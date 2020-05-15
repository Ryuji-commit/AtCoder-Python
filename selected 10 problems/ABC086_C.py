N = int(input())
start = [0, 0]
start_t = 0
for i in range(N):
    t, x, y = map(int, input().split())
    now = [x, y]
    dt = t - start_t
    dist = abs(now[0]-start[0]) + abs(now[1]-start[1])
    if dist > dt or dt % 2 != dist % 2:
        print('No')
        break
    else:
        start = now
        start_t = t
else:
    print('Yes')
