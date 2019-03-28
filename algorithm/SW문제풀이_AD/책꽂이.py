def perm(x, y, sums):
    global B, N, minN
    if x == y:
        if sums - B > 0:
            if sums - B < minN:
                minN = sums - B
    else:
        perm(x+1, y, sums)
        T[x] = True
        if sums + arr[x] - B < 0:
            perm(x+1, y, sums + arr[x])
        else:
            if sums + arr[x] - B < minN:
                minN = sums + arr[x] - B
        T[x] = False

T = int(input())
for _ in range(T):
    N, B = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    minN = 10000000
    T = [False] * N
    perm(0, N, 0)
    print(minN)
