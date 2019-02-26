import sys
sys.stdin = open('미로의거리_input.txt')

def iswall(x, y, n):
    if x < 0 or x >= n: return True
    if y < 0 or y >= n: return True
    return False

def start(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 2:
                return [i, j]

def finder(x, y):
    
    global miro, cnt, result

    if miro[x][y] == 3:
        result = cnt
        return

    miro[x][y] = 1
    cnt += 1

    if (not iswall(x+1, y, N)) and (miro[x+1][y] == 0 or miro[x+1][y] == 3):
        finder(x + 1, y)

    if (not iswall(x, y-1, N)) and (miro[x][y-1] == 0 or miro[x][y-1] == 3):
        finder(x, y - 1)

    if (not iswall(x, y+1, N)) and (miro[x][y+1] == 0 or miro[x][y+1] == 3):
        finder(x, y + 1)

    if (not iswall(x-1, y, N)) and (miro[x-1][y] == 0 or miro[x-1][y] == 3):
        finder(x - 1, y)
    
    cnt += -1

T = int(input())

for n in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for i in range(N)]
    visited = [start(miro)]
    result = 0
    cnt = 0
    finder(visited[-1][0], visited[-1][1])
    print(f'#{n} {result-1 if result else 0}')