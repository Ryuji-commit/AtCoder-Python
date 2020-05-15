N, A, B = map(int, input().split())
counter = 0
for num in range(1,N+1):
    sum_num = sum([int(i) for i in  list(str(num))])
    if sum_num >= A and sum_num <= B:
        counter += num

print(counter)
