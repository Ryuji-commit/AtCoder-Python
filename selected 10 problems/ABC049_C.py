S = reversed(input())
word = []
delete_word = ['dreamer', 'dream', 'eraser', 'erase']
for i in S:
    word += i
    if ''.join(reversed(word)) in delete_word:
        word = []

if len(word) == 0:
    print('YES')
else:
    print('NO')
