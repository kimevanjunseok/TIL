Y, X = map(int, input().split())
sy, sx, ey, ex = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(X)]
q = [[sx-1, sy-1]]
visited = [[sx-1, sy-1]]
length = len(q)
result = 0
while True:
    result += 1
    for i in range(length):
        v = q.pop(0)
        print(Y, v[0], v[1]+1)
        if v[1] + 1 < Y and arr[v[0]][v[1]+1] == 0 and [v[0], v[1]+1] not in visited:
            visited.append([v[0], v[1]+1])
            q.append([v[0], v[1]+1])
        if v[1] - 1 >= 0 and arr[v[0]][v[1]-1] == 0 and [v[0], v[1]-1] not in visited:
            visited.append([v[0], v[1] - 1])
            q.append([v[0], v[1]-1])
        if v[0] + 1 < X and arr[v[0]+1][v[1]] == 0 and [v[0]+1, v[1]] not in visited:
            visited.append([v[0]+1, v[1]])
            q.append([v[0]+1, v[1]])
        if v[0] - 1 >= 0 and arr[v[0]-1][v[1]] == 0 and [v[0]-1, v[1]] not in visited:
            visited.append([v[0]-1, v[1]])
            q.append([v[0]-1, v[1]])

    if [ex - 1, ey - 1] in q:
        break

    length = len(q)

    if not q:
        result = 0
        break

print(result)