def main():
    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    ans = a[0]
    for i in range(1, n//2):
        ans += 2*a[i]

    if n % 2 != 0:
        ans += a[i+1]

    print(ans)


if __name__ == '__main__':
    main()


