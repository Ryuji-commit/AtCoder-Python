a, b, c, k = map(int, input().split())
sum = 0
if k > a:
    k -= a
    sum += a
    if k - b > 0:
        sum -= (k - b)
else:
    sum += k

print(sum)
