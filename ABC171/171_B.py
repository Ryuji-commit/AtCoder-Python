N, K = map(int, input().split())
N_list = sorted(list(map(int, input().split())))
print(sum(N_list[:K]))

