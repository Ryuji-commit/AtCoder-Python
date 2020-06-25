i = int(input())
moji_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ans = []

while(i > 0):
    i -= 1
    ans.append(moji_list[i % 26])
    i //= 26

print(''.join(reversed(ans)))
