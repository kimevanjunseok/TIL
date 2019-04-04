def check(x, color):
    for i in range(x):
        if arr[x][i] and D[i] == color: return
    return 1

def dfs(x):
    global cnt, N, M
    if x >= N:
        cnt = 1
        return
    for i in range(1, M+1):
        if check(x, i):
            D[x] = i
            dfs(x+1)
            if cnt: return
N, M = map(int, input().split())
D = [0] * N
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

cnt = 0
dfs(0)
if cnt:
    for i in range(N):
        print(D[i], end=" ")
else:
    print(-1)