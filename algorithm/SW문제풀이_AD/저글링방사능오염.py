Y, X = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(X)]
sy, sx = map(int, input().split())
q = [[sx-1, sy-1]]
cnt = 2
arr[sx-1][sy-1] = 0
while True:
    length = len(q)
    cnt += 1
    for i in range(length):
        v = q.pop(0)
        if v[1] + 1 < Y and arr[v[0]][v[1]+1] == 1:
            arr[v[0]][v[1]+1] = 0
            q.append([v[0], v[1]+1])
        if v[1] - 1 >= 0 and arr[v[0]][v[1]-1] == 1:
            arr[v[0]][v[1] - 1] = 0
            q.append([v[0], v[1]-1])
        if v[0] + 1 < X and arr[v[0]+1][v[1]] == 1:
            arr[v[0]+1][v[1]] = 0
            q.append([v[0]+1, v[1]])
        if v[0] - 1 >= 0 and arr[v[0]-1][v[1]] == 1:
            arr[v[0]-1][v[1]] = 0
            q.append([v[0]-1, v[1]])

    if not q:
        break

zerg = 0
for i in arr:
    zerg += i.count(1)

print(cnt)
print(zerg)


