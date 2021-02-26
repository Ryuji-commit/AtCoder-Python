import collections


def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    multiple_list = set()
    counter = collections.Counter(a)
    count = 0

    for a_i in a:
        if a_i in multiple_list:
            continue

        if counter[a_i] == 1:
            count += 1

        i = 1
        while a_i * i <= a[-1]:
            multiple_list.add(a_i*i)
            i += 1
    print(count)


if __name__ == '__main__':
    main()
