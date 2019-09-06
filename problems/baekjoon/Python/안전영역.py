def BFS(height, index1, index2):
    q = [[index1, index2]]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if 0 <= ddx < n and 0 <= ddy < n and (arr[ddx][ddy] > height) and visited[ddx][ddy] != height:
                q.append([ddx, ddy])
                visited[ddx][ddy] = height

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
max_N = 0
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in arr:
    if max_N < max(i):
        max_N = max(i)

result = 1
for i in range(max_N):
    cnt = 0
    for j in range(n):
        for k in range(n):
            if (arr[j][k] > i) and visited[j][k] != i:
                visited[j][k] = i
                BFS(i, j, k)
                cnt += 1

    if cnt > result:
        result = cnt

print(result)
