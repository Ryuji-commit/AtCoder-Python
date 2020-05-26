import math

count = 0

K = int(input())
for a in range(1, K+1):
    for b in range(1, K+1):
        temp = math.gcd(a, b)
        for c in range(1, K+1):
            count += math.gcd(temp, c)

print(count)