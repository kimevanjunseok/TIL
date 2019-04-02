import sys
sys.stdin = open("보급로_input.txt")


T = int(input())

for n in range(1, T+1):
    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]
    arr = [[99999999999 for _ in range(N)] for _ in range(N)]
    q = [(0, 0)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    arr[0][0] = 0
    while q:
        x, y = q.pop(0)

        for i in range(4):
            if x+dx[i] == N-1 and y+dy[i] == N-1:
                h = board[N-1][N-1]
                if arr[x+dx[i]][y+dy[i]] > arr[x][y] + h:
                    arr[x+dx[i]][y+dy[i]] = arr[x][y] + h

            if 0<=x+dx[i]<N and 0<=y+dy[i]<N:
                h = board[x+dx[i]][y+dy[i]]
                if arr[x+dx[i]][y+dy[i]] > arr[x][y] + h:
                    arr[x+dx[i]][y+dy[i]] = arr[x][y] + h
                    q.append((x+dx[i], y+dy[i]))


    print("#{0} {1}".format(n, arr[N-1][N-1]))
