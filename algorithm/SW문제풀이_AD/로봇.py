def bfs(a, b, c):
    global X, Y, ex, ey, ed
    q = [[a, b, c, 0]]
    while q:
        x, y, d, time = q.pop(0)
        if x == ex-1 and y == ey-1 and d == ed:
            return time
        if d == 1:
            if visited[x][y][3] == 0:
                visited[x][y][3] = 1
                q.append([x, y, 3, time + 1])
                q.append([x, y, 4, time + 1])

            for i in range(1, 4):
                ay = y + i
                if 0 <= ay < Y:
                    if arr[x][ay] == 1:
                        break
                    if visited[x][ay][d-1] == 0:
                        visited[x][ay][d-1] = 1
                        q.append([x, ay, d, time + 1])
        elif d == 2:
            if visited[x][y][4] == 0:
                visited[x][y][4] = 1
                q.append([x, y, 3, time + 1])
                q.append([x, y, 4, time + 1])

            for i in range(1, 4):
                ay = y - i
                if 0 <= ay < Y:
                    if arr[x][ay] == 1:
                        break
                    if visited[x][ay][d-1] == 0:
                        visited[x][ay][d-1] = 1
                        q.append([x, ay, d, time + 1])
        elif d == 3:
            if visited[x][y][5] == 0:
                visited[x][y][5] = 1
                q.append([x, y, 1, time + 1])
                q.append([x, y, 2, time + 1])

            for i in range(1, 4):
                ax = x + i
                if 0 <= ax < X:
                    if arr[ax][y] == 1:
                        break
                    if visited[ax][y][d-1] == 0:
                        visited[ax][y][d-1] = 1
                        q.append([ax, y, d, time + 1])
        elif d == 4:
            if visited[x][y][6] == 0:
                visited[x][y][6] = 1
                q.append([x, y, 1, time + 1])
                q.append([x, y, 2, time + 1])

            for i in range(1, 4):
                ax = x - i
                if 0 <= ax < X:
                    if arr[ax][y] == 1:
                        break
                    if visited[ax][y][d-1] == 0:
                        visited[ax][y][d-1] = 1
                        q.append([ax, y, d, time + 1])

X, Y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(X)]
visited = [[[0, 0, 0, 0, 0, 0, 0] for _ in range(Y)] for _ in range(X)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())
print(bfs(sx-1, sy-1, sd))
