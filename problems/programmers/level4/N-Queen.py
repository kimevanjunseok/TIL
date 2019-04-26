def solution(N):
    def finder(x, y, N):
        for i in range(8):
            a, b = x, y
            while 0 <= a < N and 0 <= b < N:
                if arr[a][b] == 1:
                    return False
                a += dx[i]
                b += dy[i]
        return True

    def dfs(x, N):
        nonlocal cnt
        if x == N:
            cnt += 1
            return
        for i in range(N):
            if finder(x, i, N):
                arr[x][i] = 1
                dfs(x + 1, N)
                arr[x][i] = 0

    arr = [[0 for _ in range(N)] for _ in range(N)]
    dx = [0, 0, -1, 1, -1, 1, 1, -1]
    dy = [1, -1, 0, 0, 1, 1, -1, -1]
    cnt = 0
    dfs(0, N)
    return cnt