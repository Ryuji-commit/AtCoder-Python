def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0 for _ in range(401)]
    result = 0
    for a_i in a:
        cnt[a_i+200] += 1

    for i in range(401):
        for j in range(i, 401):
            result += cnt[i]*cnt[j]*((i-j)**2)
    print(result)


if __name__ == '__main__':
    main()
