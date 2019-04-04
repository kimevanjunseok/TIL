def bfs1(a, b):
    global X, Y
    q = [[a, b, 0, 0]]
    while q:
        x, y, time, cnt = q.pop(0)
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < X and 0 <= ay < Y and arr[ax][ay] != 1:
                z = 0
                if arr[ax][ay] == 2:
                    z = 1
                if visited[ax][ay] > visited[x][y] + z:
                    visited[ax][ay] = visited[x][y] + z
                    if arr[ax][ay] == 4 and visited[ax][ay] <= 3:
                        return cnt + 1
                    q.append([ax, ay, visited[x][y] + z, cnt + 1])

X, Y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(X)]
for i in range(X):
    for j in range(Y):
        if arr[i][j] == 3:
            sx = i
            sy = j
        elif arr[i][j] == 4:
            ex = i
            ey = j
visited = [[999 for _ in range(Y)] for _ in range(X)]
visited[sx][sy] = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
result = bfs1(sx, sy)
if visited[ex][ey] > 3:
    print(-1)
else:
    print(result)
