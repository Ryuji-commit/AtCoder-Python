N = int(input())
Y = int(input())

for A in range(N+1):
    for B in range(N+1):
        C = N - A - B
        if A*10000 + B*5000 + C*1000 == Y:
            print('{} {} {}'.format(A, B, C))
            quit()

print('-1 -1 -1')
