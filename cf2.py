t = int(input())
for i in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    x = 0
    for a in A:
        x ^= a
    print(x)
