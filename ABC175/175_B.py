def main():
    n = int(input())
    l_list = sorted(list(map(int, input().split())))
    count = 0
    for i in range(len(l_list)):
        for j in range(i+1, len(l_list)):
            index_i_val = l_list[i]
            index_j_val = l_list[j]
            if index_i_val == index_j_val:
                continue
            for k in range(j+1, len(l_list)):
                index_k_val = l_list[k]
                if index_k_val <= abs(index_i_val-index_j_val):
                    continue
                if index_k_val >= index_j_val + index_i_val:
                    break
                if index_i_val == index_k_val or index_j_val == index_k_val:
                    continue
                count += 1
    print(count)


if __name__ == '__main__':
    main()

