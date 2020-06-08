N = int(input())
input_list = [int(i) for i in input().split()]
max_num = 10 ** 18

sum_num = 1
if 0 in input_list:
    print('0')
else:
    for i in input_list:
        sum_num *= i
        if sum_num > max_num:
            sum_num = -1
            break
    print(sum_num)
