def main():
    s = input()
    t = input()
    min_length = len(t)
    for i in range(len(s)):
        change_length = 0
        for j in range(len(t)):
            try:
                if s[i+j] != t[j]:
                    change_length += 1
            except IndexError:
                break
        else:
            min_length = change_length if change_length < min_length else min_length
    print(min_length)


if __name__ == '__main__':
    main()
