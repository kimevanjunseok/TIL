def gogo(x, n):
    global N, M
    if n == N:
        if sum(L) == M:
            print(*L)
        L.pop()
        return
    for i in range(1, 7):
        L.append(i)
        gogo(i, n+1)
    L.pop()

N, M = map(int, input().split())

for i in range(1, 7):
    L = [i]
    gogo(i, 1)

