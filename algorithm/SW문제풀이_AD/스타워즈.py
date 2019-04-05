def func(x):
    global N

    for i in range(1, N+1):
        if board[x][i]:
            visited[x][i] = board[x][i]
    while True:
        cnt = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                if board[i][j]:
                    if visited[x][j] > board[i][j] + visited[x][i]:
                        visited[x][j] = board[i][j] + visited[x][i]
                        cnt = 1
        if not cnt:
            break


N, M, D = map(int, input().split())
board = [[0 for _ in range(N+1)] for _ in range(N+1)]
arr = []
for i in range(M):
    x, y, z = map(int, input().split())
    arr.append([x, y, z])
    board[x][y] = board[y][x] = z

visited = [[9999999999999999999999999 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    visited[i][i] = 0
    func(i)
L = [0] * (N+1)

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if visited[i][j] < D:
            cnt += 1
    L[i] = cnt

for i in visited:
    print(i)
print(max(L))

