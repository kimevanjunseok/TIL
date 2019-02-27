T = int(input())
x_y = [list(map(int, input().split())) for _ in range(T)]
arr = [[0 for _ in range(101)] for _ in range(101)]
for i in x_y:
    for j in range(i[0], i[0]+10):
        for k in range(i[1], i[1]+10):
            arr[j][k] = 1
cnt = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)