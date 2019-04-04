def bfs(a, b, s):
    arr[a][b] = "."
    q = [[a, b]]
    cnt = 0
    while cnt != len(q):
        print(q, s)
        x, y = q[cnt]
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < 12 and 0 <= ay < 6 and arr[ax][ay] == s:
                q.append([ax, ay])
                arr[ax][ay] = "."
        cnt += 1
    if len(q) < 4:
        for i in range(len(q)):
            arr[q[i][0]][q[i][1]] = s
        return 0
    else:
        return 1

def finder():
    global good
    good = 0
    for i in range(12):
        for j in range(6):
            if arr[i][j] != ".":
                a = bfs(i, j, arr[i][j])
                if a: good=1
    if good:
        after()

def after():
    global cnt
    cnt += 1
    for i in range(6):
        for j in range(11, -1, -1):
            if arr[j][i] == ".":
                x = judge(j, i)
                if x != 100:
                    arr[j][i], arr[x][i] = arr[x][i], "."

def judge(x, y):
    for i in range(x, -1, -1):
        if arr[i][y] != ".":
            return i
    return 100

T = int(input())

for N in range(T):
    arr = [list(input()) for _ in range(12)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    cnt = 0
    good = 1
    while good:
        finder()
    print(cnt)
