def main():
    k = int(input())
    seven_divided_by_k = 7 % k
    if k % 2 == 0:
        print('-1')
        return

    remainder = seven_divided_by_k
    for term in range(0, k+1):
        if remainder == 0:
            print(term+1)
            break
        remainder = (10 * remainder + seven_divided_by_k) % k
    else:
        print('-1')


if __name__ == "__main__":
    main()
