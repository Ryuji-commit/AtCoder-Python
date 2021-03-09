def return_index(val, target):
    result = [i for i, x in enumerate(target) if x == val]
    return result


def return_second(target):
    sorted_list = sorted(target)
    return sorted_list[1]


def main():
    n = int(input())
    task_a = []
    task_b = []
    for _ in range(n):
        employee = list(map(int, input().split()))
        task_a.append(employee[0])
        task_b.append(employee[1])
    if return_index(min(task_a), task_a) == return_index(min(task_b), task_b):
        second_a = return_second(task_a)
        second_b = return_second(task_b)
        select1 = max(second_a, min(task_b))
        select2 = max(min(task_a), second_b)
        select3 = min(task_a) + min(task_b)
        print(min(select1, select2, select3))
    else:
        print(max(min(task_a), min(task_b)))


if __name__ == '__main__':
    main()



