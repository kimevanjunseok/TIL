def gogo(x, y):
    global N, cnt
    arr[x][y] = cnt
    if y + 1 < N and arr[x][y+1] == 1:
        gogo(x, y+1)
    if y - 1 >= 0 and arr[x][y-1] == 1:
        gogo(x, y-1)
    if x + 1 < N and arr[x+1][y] == 1:
        gogo(x+1, y)
    if x - 1 >= 0 and arr[x-1][y] == 1:
        gogo(x-1, y)

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
cnt = 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt += 1
            gogo(i, j)

List = [0] * cnt

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            List[arr[i][j]-1] += 1

print(cnt-1)
List.sort()
for i in range(1, cnt):
    print(List[i])
for i in arr:
    print(i)



