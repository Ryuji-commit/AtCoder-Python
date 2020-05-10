x = int(input())
flag = False
for i in range(-119,119,1):
    for j in range(-119,119,1):
        if i**5 - j**5 == x:
            print('{} {}'.format(i, j))
            flag = True
            break
    if flag:
        break
