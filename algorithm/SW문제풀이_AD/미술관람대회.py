def bfs1(x, y, s):
    global N, num_N
    q = [[x, y]]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    while q:
        a, b = q.pop(0)
        for i in range(4):
            if 0 <= a + dx[i] < N and 0 <= b + dy[i] < N and arrN[a + dx[i]][b + dy[i]] == 0 and arr[a + dx[i]][b + dy[i]] == s:
                arrN[a + dx[i]][b + dy[i]] = num_N
                q.append([a + dx[i], b + dy[i]])

def bfs2(x, y, s):
    global N, num_Y
    q = [[x, y]]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    while q:
        a, b = q.pop(0)
        for i in range(4):
            if s == "R" or s == "G":
                if 0 <= a + dx[i] < N and 0 <= b + dy[i] < N and arrY[a + dx[i]][b + dy[i]] == 0 and (arr[a + dx[i]][b + dy[i]] == "G" or arr[a + dx[i]][b + dy[i]] == "R"):
                    arrY[a + dx[i]][b + dy[i]] = num_Y
                    q.append([a + dx[i], b + dy[i]])
            else:
                if 0 <= a + dx[i] < N and 0 <= b + dy[i] < N and arrY[a + dx[i]][b + dy[i]] == 0 and arr[a + dx[i]][b + dy[i]] == s:
                    arrY[a + dx[i]][b + dy[i]] = num_Y
                    q.append([a + dx[i], b + dy[i]])

N = int(input())
arr = [list(input()) for _ in range(N)]
arrN = [[0 for _ in range(N)] for _ in range(N)]
arrY = [[0 for _ in range(N)] for _ in range(N)]
num_N = 0
num_Y = 0
for i in range(N):
    for j in range(N):
        if arrN[i][j] == 0:
            num_N += 1
            arrN[i][j] = num_N
            bfs1(i, j, arr[i][j])
        
        if arrY[i][j] == 0:
            num_Y += 1
            arrY[i][j] = num_Y
            bfs2(i, j, arr[i][j])
            
print(num_N, num_Y)