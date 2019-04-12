import sys
sys.stdin = open("활주로건설_input.txt")

def func(x, y, z, a):
    global X, N
    if z == 1:
        for i in range(y, y-X, -1):
            if i < 0 or arr[x][i] != a:
                return False
        for i in range(y-X, y-X*2, -1):
            if i < 0:
                return True
            elif arr[x][i] > a:
                return False

    elif z == 2:
        for i in range(y, y+X):
            if i >= N or arr[x][i] != a:
                return False
        for i in range(y+X, y+X*2):
            if i >= N:
                return True
            elif arr[x][i] > a:
                return False

    elif z == 3:
        for i in range(x, x-X, -1):
            if i < 0 or arr[i][y] != a:
                return False
        for i in range(x-X, x-X*2, -1):
            if i < 0:
                return True
            elif arr[i][y] > a:
                return False

    elif z == 4:
        for i in range(x, x+X):
            if i >= N or arr[i][y] != a:
                return False
        for i in range(x+X, x+X*2):
            if i >= N:
                return True
            elif arr[i][y] > a:
                return False

    return True

T = int(input())

for n in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        judge1 = True
        M1 = arr[i][0]
        for j in range(1, N):
            if M1 < arr[i][j]:
                if M1+1 == arr[i][j]:
                    if func(i, j-1, 1, M1):
                        M1 = arr[i][j]
                    else:
                        judge1 = False
                else:
                    judge1 = False

            elif M1 > arr[i][j]:
                if M1-1 == arr[i][j]:
                    if func(i, j, 2, arr[i][j]):
                        M1 = arr[i][j]
                    else:
                        judge1 = False
                else:
                    judge1 = False
        if judge1 == True:
            cnt += 1

    for i in range(N):
        judge2 = True
        M2 = arr[0][i]
        for j in range(1, N):
            if M2 < arr[j][i]:
                if M2+1 == arr[j][i]:
                    if func(j-1, i, 3, M2):
                        M2 = arr[j][i]
                    else:
                        judge2 = False
                else:
                    judge2 = False

            elif M2 > arr[j][i]:
                if M2-1 == arr[j][i]:
                    if func(j, i, 4, arr[j][i]):
                        M2 = arr[j][i]
                    else:
                        judge2 = False
                else:
                    judge2 = False
        if judge2 == True:
            cnt += 1

    print("#{0} {1}".format(n, cnt))