def main():
    input_str = list(input())
    counter = 0
    max_counter = 0
    for weather in input_str:
        if weather == 'R':
            counter += 1
            if counter > max_counter:
                max_counter = counter
        else:
            counter = 0
    print(max_counter)


if __name__ == '__main__':
    main()
