X, Y = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())
arr = [[0 for _ in range(Y)] for _ in range(X)]
arr[ex-1][ey-1] = 1
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
a = abs(ex - sx)
b = abs(ey - sy)
q = [[sx-1, sy-1, 0]]
visited = [[sx-1, sy-1]]
result = 0
while q:
    x, y, time = q.pop(0)
    for i in range(8):
        if [x + dx[i], y + dy[i]] == [ex-1, ey-1]:
            result = time + 1
            break
        if 0 <= x + dx[i] < X and 0 <= y + dy[i] < Y and abs(ex - (x + dx[i])) < a+3 and abs(ey - (y + dy[i])) < b+3 and [x + dx[i], y + dy[i]] not in visited:
            visited.append([x + dx[i], y + dy[i]])
            q.append([x + dx[i], y + dy[i], time+1])
    if result:
        break
print(result)