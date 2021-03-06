def main():
    n = input()
    sum_of_term = 0
    for i in n:
        sum_of_term += int(i)
    if sum_of_term % 9 == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
