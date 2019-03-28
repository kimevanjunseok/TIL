arr = [[0 for _ in range(9)] for _ in range(10)]
R1, C1 = map(int, input().split())
R2, C2 = map(int, input().split())
dx = [[-1, -2, -3], [-1, -2, -3], [1, 2, 3], [1, 2, 3], [0, -1, -2], [0, 1, 2], [0, -1, -2], [0, 1, 2]]
dy = [[0, -1, -2], [0, 1, 2], [0, -1, -2], [0, 1, 2], [-1, -2, -3], [-1, -2, -3], [1, 2, 3], [1, 2, 3]]
q = [[R1, C1, 0]]
visited = [[R1, C1]]
result = 0
while q:
    x, y, time = q.pop(0)
    for i in range(8):
        if x + dx[i][2] == R2 and y + dy[i][2] == C2: result = time + 1
        if 0 <= x + dx[i][2] < 10 and 0 <= y + dy[i][2] < 9:
            cnt = 0
            for j in range(3):
                if [x + dx[i][j], y + dy[i][j]] == [R2, C2]:
                    cnt = 1
                    break
            if not cnt:
                q.append([x + dx[i][2], y + dy[i][2], time+1])
                visited.append([x + dx[i][2], y + dy[i][2]])

    if result:
        break

print(result) if result else print(-1)