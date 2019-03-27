Y, X = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(X)]
q = []
for i in range(X):
    for j in range(Y):
        if arr[i][j] == 1:
            q.append([i, j])

if len(q) == Y*X:
    print(0)
else:
    time = 0

    while q:
        length = len(q)
        time += 1
        for i in range(length):
            v = q.pop(0)

            if v[1] + 1 < Y and arr[v[0]][v[1]+1] == 0:
                arr[v[0]][v[1]+1] = 1
                q.append([v[0], v[1]+1])
            if v[1] - 1 >= 0 and arr[v[0]][v[1]-1] == 0:
                arr[v[0]][v[1]-1] = 1
                q.append([v[0], v[1]-1])
            if v[0] + 1 < X and arr[v[0]+1][v[1]] == 0:
                arr[v[0]+1][v[1]] = 1
                q.append([v[0]+1, v[1]])
            if v[0] - 1 >= 0 and arr[v[0]-1][v[1]] == 0:
                arr[v[0]-1][v[1]] = 1
                q.append([v[0]-1, v[1]])

    for i in arr:
        if i.count(0):
            time = 0
            break
    print(time-1)


