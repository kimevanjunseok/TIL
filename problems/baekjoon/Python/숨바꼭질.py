def BFS():
    global N, K

    q = [[N, 0]]
    p[N] = False

    while q:
        x, y = q.pop(0)
        dv = [x-1, x+1, 2*x]
        for i in range(3):
            if 0 <= dv[i] <= 200000 and p[dv[i]]:
                if dv[i] == K:
                    return y+1
                else:
                    p[dv[i]] = False
                    q.append([dv[i], y+1])


N, K = map(int, input().split())
p = [True for _ in range(200001)]
if N == K:
    print(0)
else:
    print(BFS())