def finder(x, y):
    global N
    for i in range(8):
        a, b = x, y
        while 0 <= a < N and 0 <= b < N:
            if arr[a][b] == 1:
                return False
            a += dx[i]
            b += dy[i]
    return True

def dfs(x):
    global N, cnt
    if x == N:
        cnt += 1
        return
    for i in range(N):
        if finder(x, i):
            arr[x][i] = 1
            dfs(x+1)
            arr[x][i] = 0

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]
for i in range(N):
    arr[0][i] = 1
    dfs(1)
    arr[0][i] = 0
print(cnt)