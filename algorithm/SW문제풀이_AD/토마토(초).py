Y, X, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(X*H)]
judge = 0
for i in arr:
    if i.count(0) > 0:
        judge = 1
        break
if judge:
    q = []
    for i in range(X*H):
        for j in range(Y):
            if arr[i][j] == 1:
                q.append([i, j, 0])
    dx = [0, 0, -1, 1, -X, X]
    dy = [1, -1, 0, 0, 0, 0]
    while q:
        x, y, time = q.pop(0)
        for i in range(4):
            if (x//X)*X <= x + dx[i] < (x//X)*X + X and 0 <= y + dy[i] < Y and arr[x + dx[i]][y + dy[i]] == 0: 
                arr[x + dx[i]][y + dy[i]] = 1
                q.append([x + dx[i], y + dy[i], time+1])
        for i in range(4, 6):
            if 0 <= x + dx[i] < X*H and arr[x + dx[i]][y] == 0:
                arr[x + dx[i]][y] = 1
                q.append([x + dx[i], y, time+1])
    result = time
    for i in arr:
        if i.count(0) > 0:
            result = -1
            break
    print(result)
else:
    print(0)


