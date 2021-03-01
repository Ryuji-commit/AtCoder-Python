def main():
    n = int(input())
    result = 0
    for i in range(1, n+1):
        number_of_term = n//i
        first_term = i
        last_term = first_term + (number_of_term - 1) * i
        result += 1/2*number_of_term*(first_term+last_term)
    print(int(result))


if __name__ == '__main__':
    main()
