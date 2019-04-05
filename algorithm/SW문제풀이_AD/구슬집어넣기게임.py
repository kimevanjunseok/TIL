def bfs(a, b, c, d):
    global X, Y, ex, ey
    stay = [[a, b, c, d]]
    q = [[a, b, c, d, 0]]
    while q:
        rx, ry, bx, by, time = q.pop(0)
        if time > 10:
            return -1
        if rx == ex and ry == ey:
            return time
        for i in range(4):
            rrx = rx + dx[i]
            rry = ry + dy[i]
            bbx = bx + dx[i]
            bby = by + dy[i]
            if 0 <= rrx < X and 0 <= rry < Y and 0 <= bbx < X and 0 <= bby < Y:
                if arr[rrx][rry] != "#" and arr[bbx][bby] == "#" and (not (rrx == bx and rry == by)) and [rrx, rry, bx, by] not in stay and arr[bx][by] != "H":
                    stay.append([rrx, rry, bx, by])
                    q.append([rrx, rry, bx, by, time + 1])
                elif arr[rrx][rry] == "#" and arr[bbx][bby] != "#" and (not (rx == bbx and ry == bby)) and [rx, ry, bbx, bby] not in stay and arr[bbx][bby] != "H":
                    stay.append([rx, ry, bbx, bby])
                    q.append([rx, ry, bbx, bby, time + 1])
                elif arr[rrx][rry] != "#" and arr[bbx][bby] != "#" and (not (rrx == bbx and rry == bby)) and [rrx, rry, bbx, bby] not in stay and arr[bbx][bby] != "H":
                    stay.append([rrx, rry, bbx, bby])
                    q.append([rrx, rry, bbx, bby, time + 1])
    return -1

T = int(input())

for n in range(T):
    X, Y = map(int, input().split())
    arr = [list(input()) for _ in range(X)]

    for i in range(X):
        for j in range(Y):
            if arr[i][j] == "R":
                arr[i][j] = "."
                w, x = i, j
            elif arr[i][j] == "B":
                arr[i][j] = "."
                y, z = i, j
            elif arr[i][j] == "H":
                ex, ey = i, j

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    print(bfs(w, x, y, z))