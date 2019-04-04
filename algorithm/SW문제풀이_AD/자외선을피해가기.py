N = int(input())
board = [list(map(int, list(input()))) for _ in range(N)]
visited = [[99999999999 for _ in range(N)] for _ in range(N)]
visited[0][0] = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = [[0, 0]]
while q:
    x, y = q.pop(0)
    for i in range(4):
        if 0<=x+dx[i]<N and 0<=y+dy[i]<N:
            if visited[x+dx[i]][y+dy[i]] > board[x+dx[i]][y+dy[i]] + visited[x][y]:
                visited[x+dx[i]][y+dy[i]] = board[x+dx[i]][y+dy[i]] + visited[x][y]
                q.append([x+dx[i], y+dy[i]])
print(visited[N-1][N-1])
