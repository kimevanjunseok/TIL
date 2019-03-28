def perm(x, y, sums):
    global K, result
    if result:
        return
    if x == y:
        if sums == K:
            result = 1
            return

    else:
        perm(x+1, y, sums)
        T[x] = True
        if sums+di[x] <= K:
            perm(x+1, y, sums+di[x])
        T[x] = False


T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    di = list(map(int, input().split()))
    T = [False] * N
    result = 0
    perm(0, N, 0)
    if result:
        print("YES")
    else:
        print("NO")
