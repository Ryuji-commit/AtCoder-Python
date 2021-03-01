import copy


# ここら辺はライブラリで求めるのが正解
def combination(num):
    result_combination = [[0]]
    recursion([], 1, num, result_combination)
    return result_combination


def recursion(combination_list, i, max_num, result_combination):
    if i > max_num:
        if len(combination_list) > 0:
            result_combination.append(combination_list)
        return
    new_list = combination_list + [i]
    recursion(new_list, i+1, max_num, result_combination)
    recursion(combination_list, i+1, max_num, result_combination)


def fill_table(line_list, row_list, h, w, table):
    count = 0
    copied_table = copy.deepcopy(table)

    for line in line_list:
        if line == 0:
            continue
        for row in range(w):
            copied_table[line-1][row] = '.'
    for row in row_list:
        if row == 0:
            continue
        for line in range(h):
            copied_table[line][row-1] = '.'
    for line in range(h):
        for row in range(w):
            if copied_table[line][row] == '#':
                count += 1
    return count


def main():
    h, w, k = map(int, input().split())
    table = []
    for _ in range(h):
        table.append(list(input()))
    result = 0
    combination_h = combination(h)
    combination_w = combination(w)
    for line_list in combination_h:
        for row_list in combination_w:
            if fill_table(line_list, row_list, h, w, table) == k:
                result += 1
    print(result)


if __name__ == '__main__':
    main()
