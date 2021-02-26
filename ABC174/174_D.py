def main():
    stone_nums = int(input())
    stones = list(input())
    red_stone_nums = stones.count('R')
    print(stones[red_stone_nums:].count('R'))


if __name__ == '__main__':
    main()
