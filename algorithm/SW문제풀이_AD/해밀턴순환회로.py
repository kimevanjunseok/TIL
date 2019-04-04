def dfs(x, y, z):
    global N, minN
    if y == N:
        if arr[x][0]:
            z = z+arr[x][0]
            if z < minN:
                minN = z
        return
    for i in range(1, N):
        if arr[x][i] and not D[i]:
            D[i] = 1
            dfs(i, y+1, z+arr[x][i])
            D[i] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
minN = 999999999
D = [0] * N
dfs(0, 1, 0)
print(minN) if minN != 999999999 else print(0)