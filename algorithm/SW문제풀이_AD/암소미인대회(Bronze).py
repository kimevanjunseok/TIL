def bfs(a, b, c):
    global X, Y
    q = [[a, b]]
    arr[a][b] = c
    while q:
        x, y = q.pop(0)
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < X and 0 <= ay < Y and arr[ax][ay] == "X":
                arr[ax][ay] = c
                q.append([ax, ay])


X, Y = map(int, input().split())
arr = [list(input()) for _ in range(X)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = "1"
for i in range(X):
    for j in range(Y):
        if arr[i][j] == "X":
            bfs(i, j, cnt)
            cnt = "2"

L1 = []
L2 = []
minN = 99999999999999999999
for i in range(X):
    for j in range(Y):
        if arr[i][j] == "1":
            L1.append([i, j])
        elif arr[i][j] == "2":
            L2.append([i, j])
for i in arr:
    print(i)

for i in range(len(L1)):
    for j in range(len(L2)):
        if abs(L1[i][0] - L2[j][0]) + abs(L1[i][1] - L2[j][1]) < minN:
            minN = abs(L1[i][0] - L2[j][0]) + abs(L1[i][1] - L2[j][1])
print(minN-1)




