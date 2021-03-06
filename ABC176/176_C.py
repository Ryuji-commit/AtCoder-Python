def main():
    n = int(input())
    a = list(map(int, input().split()))
    border = 0
    result = 0
    for a_i in a:
        if border < a_i:
            border = a_i
        result += border - a_i
    print(result)


if __name__ == '__main__':
    main()
