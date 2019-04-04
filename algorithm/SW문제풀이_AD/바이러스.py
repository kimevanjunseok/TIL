def func(x):
    global result
    D[x] = 1
    result += 1
    for i in range(1, N+1):
        if arr[x][i] and (not D[i]):
            func(i)

N = int(input())
M = int(input())
arr = [[0] *(N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    arr[x][y] = arr[y][x] = 1
D = [0] * (N+1)
result = 0
func(1)
print(result-1)
