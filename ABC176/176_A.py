def main():
    n, x, t = map(int, input().split())
    total_time = n//x*t
    if n % x != 0:
        total_time += t
    print(total_time)


if __name__ == '__main__':
    main()
