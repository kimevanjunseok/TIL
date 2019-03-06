import sys
sys.stdin = open('핀볼게임_input.txt')

def right(x, y):
    global cnt, result, count
    count += 1

    while True:
        x += dx[0]
        y += dy[0]
        if count > 1:
            if [x, y] in visited:
                break
        if arr[x][y] != 0:
            break
    if arr[x][y] == 0:
        if result < cnt:
            result = cnt
        cnt = 0
        return
    elif arr[x][y] == 1 or arr[x][y] == 2 or arr[x][y] == 5:
        cnt += 1
        return left(x, y)
    elif arr[x][y] == 3:
        cnt += 1
        return down(x, y)
    elif arr[x][y] == 4:
        cnt += 1
        return up(x, y)
    elif 6 <= arr[x][y] <= 10:
        head = finder(x, y, arr[x][y])
        return right(head[0], head[1])
    elif arr[x][y] == -1:
        if result < cnt:
            result = cnt
        cnt = 0
        return


def left(x, y):
    global cnt, result, count
    count += 1
    while True:
        x += dx[1]
        y += dy[1]
        if count > 1:
            if [x, y] in visited:
                break
        if arr[x][y] != 0:
            break
    if arr[x][y] == 0:
        if result < cnt:
            result = cnt
        cnt = 0
        return
    elif arr[x][y] == 3 or arr[x][y] == 4 or arr[x][y] == 5:
        cnt += 1
        return right(x, y)
    elif arr[x][y] == 2:
        cnt += 1
        return down(x, y)
    elif arr[x][y] == 1:
        cnt += 1
        return up(x, y)
    elif 6 <= arr[x][y] <= 10:
        head = finder(x, y, arr[x][y])
        return left(head[0], head[1])
    elif arr[x][y] == -1:
        if result < cnt:
            result = cnt
        cnt = 0
        return

def up(x, y):
    global cnt, result, count
    count += 1
    while True:
        x += dx[2]
        y += dy[2]
        if count > 1:
            if [x, y] in visited:
                break
        if arr[x][y] != 0:
            break
    if arr[x][y] == 0:
        if result < cnt:
            result = cnt
        cnt = 0
        return
    elif arr[x][y] == 1 or arr[x][y] == 4 or arr[x][y] == 5:
        cnt += 1
        return down(x, y)
    elif arr[x][y] == 2:
        cnt += 1
        return right(x, y)
    elif arr[x][y] == 3:
        cnt += 1
        return left(x, y)
    elif 6 <= arr[x][y] <= 10:
        head = finder(x, y, arr[x][y])
        return up(head[0], head[1])
    elif arr[x][y] == -1:
        if result < cnt:
            result = cnt
        cnt = 0
        return

def down(x, y):
    global cnt, result, count
    count += 1
    while True:
        x += dx[3]
        y += dy[3]
        if count > 1:
            if [x, y] in visited:
                break
        if arr[x][y] != 0:
            break
    if arr[x][y] == 0:
        if result < cnt:
            result = cnt
        cnt = 0
        return
    elif arr[x][y] == 2 or arr[x][y] == 3 or arr[x][y] == 5:
        cnt += 1
        return up(x, y)
    elif arr[x][y] == 1:
        cnt += 1
        return right(x, y)
    elif arr[x][y] == 4:
        cnt += 1
        return left(x, y)
    elif 6 <= arr[x][y] <= 10:
        head = finder(x, y, arr[x][y])
        return down(head[0], head[1])
    elif arr[x][y] == -1:
        if result < cnt:
            result = cnt
        cnt = 0
        return

def finder(x, y, z):
    global N
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == z:
                if x != i or y != j:
                    return [i, j]

T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for n in range(1, T+1):
    N = int(input())
    arr = [[5] * (N+2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5] * (N+2)]
    result = 0
    visited = []
    cnt = 0
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 0:

                visited.append([i, j])

                right(i, j)

                left(i, j)

                down(i, j)

                up(i, j)

                visited.pop()
    print("#{0} {1}".format(n, result))


