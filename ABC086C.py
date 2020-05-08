n = int(input())
start = [0, 0, 0]


def check_d(start, end):
    time_d = end[0] - start[0]
    range_d = abs(start[1]-end[1]) + abs(start[2]-end[2])
    return time_d, range_d


for i in range(n):
    end = list(map(int, input().split()))
    ans = check_d(start, end)
    start = end
    if ans[0] < ans[1] or (ans[0]+ans[1]) % 2 != 0:
        print('No')
        quit()

print('Yes')