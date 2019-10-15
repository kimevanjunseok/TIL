def solution(N):
    def finder(x, y, N):
        for i in range(4):
            a, b = x, y
            while 0 <= a < N and 0 <= b < N:
                if arr[a][b] == 1:
                    return False
                a += dx[i]
                b += dy[i]
        return True

    def dfs(x, N, L):
        nonlocal cnt
        if x == N:
            cnt += 1
            return
        for i in range(N):
            if L[i] == 0 and finder(x, i, N):
                arr[x][i] = 1
                L[i] = 1
                dfs(x + 1, N, L)
                arr[x][i] = 0
                L[i] = 0

    arr = [[0 for _ in range(N)] for _ in range(N)]
    dx = [-1, 1, 1, -1]
    dy = [1, 1, -1, -1]
    cnt = 0
    L = [0] * N
    dfs(0, N, L)

    return cnt

if __name__ == "__main__":
    N = [4, 12]
    for i in range(2):
        print(solution(N[i]))