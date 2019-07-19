def judge(x1, y1, x2, y2, value):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if board[i][j] > value:
                return False
    return True

X, Y, S = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(S)]
board = [[0 for _ in range(Y)] for _ in range(X)]

for i in range(S):
    x1 = arr[i][0]
    y1 = arr[i][1]
    x2 = arr[i][2]
    y2 = arr[i][3]
    value = arr[i][4]
    if judge(x1, y1, x2, y2, value):
        for j in range(x1, x2 + 1):
            for k in range(y1, y2 + 1):
                board[j][k] = value

max_value = 0

for i in board:
    if max(i) > max_value:
        max_value = max(i)

cnt = 0

for i in board:
    for j in i:
        if j == max_value:
            cnt += 1

print(cnt)