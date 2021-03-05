def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    result = x % d
    result_sub = abs(result-d)
    result_num = x // d
    if result > abs(result-d):
        result_sub = result
        result = abs(result-d)
        result_num += 1

    if k < result_num:
        result = x
        result -= d * k
        print(result)
        return

    if result_num % 2 == k % 2:
        print(result)
    else:
        print(result_sub)


if __name__ == '__main__':
    main()
