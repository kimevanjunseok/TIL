import sys
sys.stdin = open("최소비용_input.txt")

def BFS():
    global N

    q = [[0, 0]]
    visited[0][0] = 0
    while q:
        x, y = q.pop(0)
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < N and 0 <= ay < N:
                sums = 0
                if arr[x][y] < arr[ax][ay]:
                    sums = arr[ax][ay] - arr[x][y]
                
                if sums + visited[x][y] + 1 < visited[ax][ay]:
                    q.append([ax, ay])
                    visited[ax][ay] = sums + visited[x][y] + 1

T = int(input())

for n in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[999999999 for _ in range(N)] for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    BFS()
    print("#{} {}".format(n, visited[N-1][N-1]))