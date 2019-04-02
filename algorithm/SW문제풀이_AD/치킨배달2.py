def combi(x, y):
    global minN
    if y == 0:
        L = [i for i in T]
        d = bfs(L)
        if d < minN:
            minN = d
    elif x < y :
        return
    else:
        T[y-1] = home[x-1]
        combi(x-1, y-1)
        combi(x-1, y)

def bfs(q):
    global N, minN, one_cnt
    visited = []
    length = []
    come = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        x, y, z = q.pop(0)
        come.append([x, y])
        if sum(length) > minN or len(length) == one_cnt:
            break
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < N and 0 <= ay < N and arr[ax][ay] == 1 and [ax, ay] not in visited:
                visited.append([ax, ay])
                length.append(z+1)

            elif 0 <= ax < N and 0 <= ay < N and [ax, ay] not in come:
                q.append([ax, ay, z+1])
    return sum(length)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
home = []
one_cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            home.append([i, j, 0])
        elif arr[i][j] == 1:
            one_cnt += 1
minN = 999999999999
for i in range(1, M+1):
    T = [[]] * i
    combi(len(home), i)

print(minN)