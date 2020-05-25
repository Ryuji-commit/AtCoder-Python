N = int(input())
A = list(map(int, input().split()))
buka = [0] * N

for i in A:
    buka[i-1] += 1

t = [print(i) for i in buka]
