N = int(input())

arr = [list(map(int, list(input()))) for _ in range(N)]

cnt = 1
save = []
max_num = 0
com = -1

for i in range(0, N):
    for j in range(0, N):
        if arr[i][j] == 1:
            max_num = 1
            break

while True:
    com = max_num
    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j] == cnt and arr[i+1][j] != 0 and arr[i-1][j] != 0 and arr[i][j+1] != 0 and arr[i][j-1] != 0:
                save = [arr[i+1][j], arr[i-1][j], arr[i][j+1], arr[i][j-1]]
                arr[i][j] = min(save) + 1

            if arr[i][j] > max_num:
                max_num = arr[i][j]
    cnt += 1
    if com == max_num:
        break

print(max_num)
