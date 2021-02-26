X, Y = map(int, input().split())
for turtle in range(X+1):
    leg_num = turtle * 4 + (X-turtle) * 2
    if Y == leg_num:
        print('Yes')
        quit()
print('No')
