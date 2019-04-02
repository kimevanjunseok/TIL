import sys
sys.stdin = open("최소비용_input.txt")


T = int(input())

for n in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[99999999999 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = [(0, 0)]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            if 0<=x+dx[i]<N and 0<=y+dy[i]<N:
                h = 0
                if board[x+dx[i]][y+dy[i]] > board[x][y]:
                    h = board[x+dx[i]][y+dy[i]] - board[x][y]
                if visited[x+dx[i]][y+dy[i]] > visited[x][y] + h + 1:
                    visited[x+dx[i]][y+dy[i]] = visited[x][y] + h + 1
                    q.append((x+dx[i], y+dy[i]))
    print("#{0} {1}".format(n, visited[N-1][N-1]))









