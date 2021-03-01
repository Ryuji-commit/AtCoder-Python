N = int(input())
counter_val = ['AC', 'WA', 'TLE', 'RE']
counter = [0, 0, 0, 0]  # [AC, WA, TLE, RE]
LenOfCounter = 4

for _ in range(N):
    S = input()
    for i in range(LenOfCounter):
        if counter_val[i] == S:
            counter[i] += 1

for i in range(LenOfCounter):
    print('{} x {}'.format(counter_val[i], counter[i]))
