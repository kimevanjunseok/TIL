def combi(x, y):
    global minN
    if y == 0:
        d = func([i for i in T])
        if d < minN:
            minN = d

    elif x < y:
        return
    else:
        T[y-1] = home[x-1]
        combi(x-1, y-1)
        combi(x-1, y)

def func(q):
    global N
    sums = 0
    for i in one_cnt:
        cnt = []
        for j in q:
            cnt.append(abs(i[0] - j[0]) + abs(i[1] - j[1]))
        sums += min(cnt)
    return sums

N, M = map(int, input().split())
arr = []
home = []
one_cnt = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] == 2:
            home.append([i, j, 0])
        elif arr[i][j] == 1:
            one_cnt.append([i, j])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
minN = 999999999999
if len(home) > M:
    T = [0] * M
    combi(len(home), M)
else:
    minN = func(home)

print(minN)
