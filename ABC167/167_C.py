# 再帰で全ての組み合わせを求める
def my_loop(n_counter, my_list):
    if n_counter == N:
        bool_list = [i >= X for i in my_list[1:]]
        if all(bool_list):
            ans.append(my_list[0])
    else:
        # 要素同士を足す
        add_list = [my_list[i] + temp[n_counter][i] for i in range(M+1)]
        my_loop(n_counter+1, my_list)
        my_loop(n_counter+1, add_list)


N, M, X = map(int, input().split())
temp = []
ans = []
for _ in range(N):
    temp.append(list(map(int, input().split())))

my_loop(0, [0]*(M+1))
print(min(ans) if len(ans) != 0 else '-1')

