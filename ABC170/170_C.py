X, N = map(int, input().split())
p_list = list(map(int, input().split()))
abs_num = 0


def func(near):
    if near not in p_list:
        print(near)
        quit()


while(True):
    near = X - abs_num
    func(near)
    near = X + abs_num
    func(near)
    abs_num += 1
