N, M = map(int, input().split())
Ai = list(map(int, input().split()))
border = 1/(4*M) * sum(Ai)
Bi = [i for i in Ai if i >= border]

if M <= len(Bi):
    print('Yes')
else:
    print('No')


