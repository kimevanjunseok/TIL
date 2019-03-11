import sys
sys.stdin = open('재미있는오셀로게임_input.txt')

T = int(input())

def turn(L):
    global board

    if L[2] == 1:
        board[L[0]][L[1]] = 'B'
        change_2(L[0], L[1], 0)

    elif L[2] == 2:
        board[L[0]][L[1]] = 'W'
        change_2(L[0], L[1], 1)

def change_2(x, y, s):
    global board, N, dx, dy, String

    index = 0

    while index != 8:
        if board[x + dx[index]][y + dy[index]] == String[s+1]:
            a = 0
            for i in range(1, N + 2):
                if board[x + dx[index] * i][y + dy[index] * i] == 0:
                    a = 0
                    break
                if board[x + dx[index] * i][y + dy[index] * i] == String[s+1]:
                    a += 1
                if board[x + dx[index] * i][y + dy[index] * i] == String[s]:
                    break
            for i in range(1, a+1):
                board[x + dx[index] * i][y + dy[index] * i] = String[s]

        index += 1

def change_1(x, y, s):
    global board, N, dx, dy

    index = 0

    if s == 'B':
        while index != 8:
            if board[x + dx[index]][y + dy[index]] == 'W':
                a = 0
                for i in range(1, N + 2):
                    if board[x + dx[index] * i][y + dy[index] * i] == 0:
                        a = 0
                        break
                    if board[x + dx[index] * i][y + dy[index] * i] == 'W':
                        a += 1
                    if board[x + dx[index] * i][y + dy[index] * i] == 'B':
                        break
                for i in range(1, a+1):
                    board[x + dx[index] * i][y + dy[index] * i] = 'B'

            index += 1

    elif s == 'W':
        while index != 8:
            if board[x + dx[index]][y + dy[index]] == 'B':
                a = 0
                for i in range(1, N + 2):
                    if board[x + dx[index] * i][y + dy[index] * i] == 0:
                        a = 0
                        break
                    if board[x + dx[index] * i][y + dy[index] * i] == 'B':
                        a += 1
                    if board[x + dx[index] * i][y + dy[index] * i] == 'W':
                        break
                for i in range(1, a+1):
                    board[x + dx[index] * i][y + dy[index] * i] = 'W'

            index += 1

def change(x, y, s):
    global board, N

    if s == 'B':
        if board[x][y + 1] == 'W':
            a = 0
            for i in range(y+1, N+2):
                if board[x][i] == 0:
                    a = 0
                    break
                if board[x][i] == 'W':
                    a += 1
                if board[x][i] == 'B':
                    break
            for i in range(a):
                board[x][y+1+i] = 'B'

        if board[x][y - 1] == 'W':
            a = 0
            for i in range(y - 1, -1, -1):
                if board[x][i] == 0:
                    a = 0
                    break
                if board[x][i] == 'W':
                    a += 1
                if board[x][i] == 'B':
                    break
            for i in range(a):
                board[x][y-1-i] = 'B'

        if board[x + 1][y] == 'W':
            a = 0
            for i in range(x + 1, N+2):
                if board[i][y] == 0:
                    a = 0
                    break
                if board[i][y] == 'W':
                    a += 1
                if board[i][y] == 'B':
                    break
            for i in range(a):
                board[x+1+i][y] = 'B'

        if board[x - 1][y] == 'W':
            a = 0
            for i in range(x - 1, -1, -1):
                if board[i][y] == 0:
                    a = 0
                    break
                if board[i][y] == 'W':
                    a += 1
                if board[i][y] == 'B':
                    break
            for i in range(a):
                board[x-1-i][y] = 'B'

        if board[x - 1][y - 1] == 'W':
            a = 0
            for i in range(N+2):
                if board[x-1-i][y-1-i] == 0:
                    a = 0
                    break
                if board[x-1-i][y-1-i] == 'B':
                    break
                if board[x-1-i][y-1-i] == "W":
                    a += 1
            for i in range(a):
                board[x-1-i][y-1-i] = 'B'

        if board[x + 1][y + 1] == 'W':
            a = 0
            for i in range(N+2):
                if board[x+1+i][y+1+i] == 0:
                    a = 0
                    break
                if board[x+1+i][y+1+i] == 'B':
                    break
                if board[x+1+i][y+1+i] == "W":
                    a += 1
            for i in range(a):
                board[x+1+i][y+1+i] = 'B'

        if board[x + 1][y - 1] == 'W':
            a = 0
            for i in range(N+2):
                if board[x+1+i][y-1-i] == 0:
                    a = 0
                    break
                if board[x+1+i][y-1-i] == 'B':
                    break
                if board[x+1+i][y-1-i] == "W":
                    a += 1
            for i in range(a):
                board[x+1+i][y-1-i] = 'B'

        if board[x - 1][y + 1] == 'W':
            a = 0
            for i in range(N+2):
                if board[x-1-i][y+1+i] == 0:
                    a = 0
                    break
                if board[x-1-i][y+1+i] == 'B':
                    break
                if board[x-1-i][y+1+i] == "W":
                    a += 1
            for i in range(a):
                board[x-1-i][y+1+i] = 'B'


    elif s == 'W':
        if board[x][y + 1] == 'B':
            a = 0
            for i in range(y+1, N+2):
                if board[x][i] == 0:
                    a = 0
                    break
                if board[x][i] == 'W':
                    break
                if board[x][i] == 'B':
                    a += 1
            for i in range(a):
                board[x][y+1+i] = 'W'

        if board[x][y - 1] == 'B':
            a = 0
            for i in range(y - 1, -1, -1):
                if board[x][i] == 0:
                    a = 0
                    break
                if board[x][i] == 'W':
                    break
                if board[x][i] == 'B':
                    a += 1
            for i in range(a):
                board[x][y-1-i] = 'W'

        if board[x + 1][y] == 'B':
            a = 0
            for i in range(x + 1, N+2):
                if board[i][y] == 0:
                    a = 0
                    break
                if board[i][y] == 'W':
                    break
                if board[i][y] == 'B':
                    a += 1
            for i in range(a):
                board[x+1+i][y] = 'W'

        if board[x - 1][y] == 'B':
            a = 0
            for i in range(x - 1, -1, -1):
                if board[i][y] == 0:
                    a = 0
                    break
                if board[i][y] == 'W':
                    break
                if board[i][y] == 'B':
                    a += 1
            for i in range(a):
                board[x-1-i][y] = 'W'

        if board[x - 1][y - 1] == 'B':
            a = 0
            for i in range(N + 2):
                if board[x - 1 - i][y - 1 - i] == 0:
                    a = 0
                    break
                if board[x - 1 - i][y - 1 - i] == 'W':
                    break
                if board[x-1-i][y-1-i] == "B":
                    a += 1
            for i in range(a):
                board[x - 1 - i][y - 1 - i] = 'W'

        if board[x + 1][y + 1] == 'B':
            a = 0
            for i in range(N + 2):
                if board[x + 1 + i][y + 1 + i] == 0:
                    a = 0
                    break
                if board[x + 1 + i][y + 1 + i] == 'W':
                    break
                if board[x+1+i][y+1+i] == "B":
                    a += 1
            for i in range(a):
                board[x + 1 + i][y + 1 + i] = 'W'

        if board[x + 1][y - 1] == 'B':
            a = 0
            for i in range(N + 2):
                if board[x + 1 + i][y - 1 - i] == 0:
                    a = 0
                    break
                if board[x + 1 + i][y - 1 - i] == 'W':
                    break
                if board[x+1+i][y-1-i] == "B":
                    a += 1
            for i in range(a):
                board[x + 1 + i][y - 1 - i] = 'W'

        if board[x - 1][y + 1] == 'B':
            a = 0
            for i in range(N + 2):
                if board[x - 1 - i][y + 1 + i] == 0:
                    a = 0
                    break
                if board[x - 1 - i][y + 1 + i] == 'W':
                    break
                if board[x-1-i][y+1+i] == "B":
                    a += 1
            for i in range(a):
                board[x - 1 - i][y + 1 + i] = 'W'

for n in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(M)]

    board[N // 2 -1][N // 2 - 1] = board[N // 2][N // 2] = 'W'
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 'B'

    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    String = ['B', 'W', 'B']

    for i in range(len(board)):
        board[i] = [0] + board[i] + [0]

    board = [[0] * (N+2)] + board + [[0] * (N+2)]

    for i in range(len(arr)):
        turn(arr[i])

    B = 0
    W = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 'B':
                B += 1
            elif board[i][j] == 'W':
                W += 1

    print('#{0} {1} {2}'.format(n, B, W))