def main():
    a, b = map(int, input().split())
    kokei = a + b
    sibou = b
    if kokei >= 15 and sibou >= 8:
        print(1)
    elif kokei >= 10 and sibou >= 3:
        print(2)
    elif kokei >= 3:
        print(3)
    else:
        print(4)


if __name__ == '__main__':
    main()
