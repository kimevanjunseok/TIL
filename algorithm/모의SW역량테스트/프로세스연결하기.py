import sys
sys.stdin = open('프로세스연결하기_input.txt')

def center(z):

    global arr, location, N, one_ea, min_num

    if z == len(location):
        number = 0
        for i in range(N):
            number += arr[i].count(1)
        number = number - one_ea
        if number < min_num:
            min_num = number
        return

    right(location[z][0], location[z][1]+1, z)
    left(location[z][0], location[z][1]-1, z)
    up(location[z][0]-1, location[z][1], z)
    down(location[z][0]+1, location[z][1], z)

def right(x, y, z):
    global arr

    if y == N:
        center(z+1)

    elif arr[x][y] == 0:
        arr[x][y] = 1
        right(x, y+1, z)
        arr[x][y] = 0

    elif arr[x][y] != 0:
        return

def left(x, y, z):
    global arr

    if y == -1:
        center(z+1)

    elif arr[x][y] == 0:
        arr[x][y] = 1
        left(x, y-1, z)
        arr[x][y] = 0

    elif arr[x][y] != 0:
        return

def up(x, y, z):
    global arr

    if x == -1:
        center(z+1)

    elif arr[x][y] == 0:
        arr[x][y] = 1
        up(x-1, y, z)
        arr[x][y] = 0

    elif arr[x][y] != 0:
        return

def down(x, y, z):
    global arr

    if x == N:
        center(z+1)

    elif arr[x][y] == 0:
        arr[x][y] = 1
        down(x+1, y, z)
        arr[x][y] = 0

    elif arr[x][y] != 0:
        return

def judge(x, y):
    global arr

    cnt = 0

    b = y
    while b != N-1:
        b += 1
        if arr[x][b] != 0:
            cnt += 1
            break
    b = y
    while b != 0:
        b += -1
        if arr[x][b] != 0:
            cnt += 1
            break
    a = x
    while a != N-1:
        a += 1
        if arr[a][y] != 0:
            cnt += 1
            break
    a = x
    while a != 0:
        a += -1
        if arr[a][y] != 0:
            cnt += 1
            break

    if cnt == 4:
        return False
    else:
        return True

T = int(input())

for n in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    location = []

    for i in range(1, N-1):
        for j in range(1, N-1):
            if (arr[i][j] == 1) and judge(i, j):
                location.append([i, j])

    one_ea = 0
    for i in range(N):
        one_ea += arr[i].count(1)

    min_num = 999999999999999
    center(0)

    print("#{0} {1}".format(n, min_num))