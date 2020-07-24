t = int(input())
for i in range(t):
    n, m = map(int, input().split(' '))
    A = [int(i) for i in input().split(' ')]
    B = [int(i) for i in input().split(' ')]
    di = dict()
    for a in A:
        di[a] = 1
    ans = -1
    for b in B:
        if di.get(b, 0) == 1:
            ans = b
            break
    if ans == -1:
        print('NO')
    else:
        print('YES')
        print('{} {}'.format(1, ans))
            
