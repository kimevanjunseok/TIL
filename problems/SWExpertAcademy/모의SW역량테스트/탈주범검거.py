import sys
sys.stdin = open('탈주범검거_input.txt')

def center(x, y, z):
    global N, M, bfs

    if z == 1:
        if (y + 1 < M) and ([x, y+1] not in visited) and (arr[x][y+1] == 1 or arr[x][y+1] == 3 or arr[x][y+1] == 6 or arr[x][y+1] == 7):
            bfs.append([x, y + 1, arr[x][y+1]])
        
        if (0 <= y - 1) and ([x, y-1] not in visited) and (arr[x][y-1] == 1 or arr[x][y-1] == 3 or arr[x][y-1] == 4 or arr[x][y-1] == 5):
            bfs.append([x, y - 1, arr[x][y-1]])
        
        if (x + 1 < N) and ([x+1, y] not in visited) and (arr[x+1][y] == 1 or arr[x+1][y] == 2 or arr[x+1][y] == 4 or arr[x+1][y] == 7):
            bfs.append([x + 1, y, arr[x+1][y]])

        if (0 <= x - 1) and ([x-1, y] not in visited) and (arr[x-1][y] == 1 or arr[x-1][y] == 2 or arr[x-1][y] == 5 or arr[x-1][y] == 6):
            bfs.append([x - 1, y, arr[x-1][y]])

    elif z == 2:
        if (x + 1 < N) and ([x+1, y] not in visited) and (arr[x+1][y] == 1 or arr[x+1][y] == 2 or arr[x+1][y] == 4 or arr[x+1][y] == 7):
            bfs.append([x + 1, y, arr[x+1][y]])

        if (0 <= x - 1) and ([x-1, y] not in visited) and (arr[x-1][y] == 1 or arr[x-1][y] == 2 or arr[x-1][y] == 5 or arr[x-1][y] == 6):
            bfs.append([x - 1, y, arr[x-1][y]])

    elif z == 3:
        if (y + 1 < M) and ([x, y+1] not in visited) and (arr[x][y+1] == 1 or arr[x][y+1] == 3 or arr[x][y+1] == 6 or arr[x][y+1] == 7):
            bfs.append([x, y + 1, arr[x][y+1]])
        
        if (0 <= y - 1) and ([x, y-1] not in visited) and (arr[x][y-1] == 1 or arr[x][y-1] == 3 or arr[x][y-1] == 4 or arr[x][y-1] == 5):
            bfs.append([x, y - 1, arr[x][y-1]])
        
    elif z == 4:
        if (y + 1 < M) and ([x, y+1] not in visited) and (arr[x][y+1] == 1 or arr[x][y+1] == 3 or arr[x][y+1] == 6 or arr[x][y+1] == 7):
            bfs.append([x, y + 1, arr[x][y+1]])
        
        if (0 <= x - 1) and ([x-1, y] not in visited) and (arr[x-1][y] == 1 or arr[x-1][y] == 2 or arr[x-1][y] == 5 or arr[x-1][y] == 6):
            bfs.append([x - 1, y, arr[x-1][y]])

    elif z == 5:
        if (y + 1 < M) and ([x, y+1] not in visited) and (arr[x][y+1] == 1 or arr[x][y+1] == 3 or arr[x][y+1] == 6 or arr[x][y+1] == 7):
            bfs.append([x, y + 1, arr[x][y+1]])

        if (x + 1 < N) and ([x+1, y] not in visited) and (arr[x+1][y] == 1 or arr[x+1][y] == 2 or arr[x+1][y] == 4 or arr[x+1][y] == 7):
            bfs.append([x + 1, y, arr[x+1][y]])

    elif z == 6:
        if (0 <= y - 1) and ([x, y-1] not in visited) and (arr[x][y-1] == 1 or arr[x][y-1] == 3 or arr[x][y-1] == 4 or arr[x][y-1] == 5):
            bfs.append([x, y - 1, arr[x][y-1]])
        
        if (x + 1 < N) and ([x+1, y] not in visited) and (arr[x+1][y] == 1 or arr[x+1][y] == 2 or arr[x+1][y] == 4 or arr[x+1][y] == 7):
            bfs.append([x + 1, y, arr[x+1][y]])

    elif z == 7:
        if (0 <= y - 1) and ([x, y-1] not in visited) and (arr[x][y-1] == 1 or arr[x][y-1] == 3 or arr[x][y-1] == 4 or arr[x][y-1] == 5):
            bfs.append([x, y - 1, arr[x][y-1]])

        if (0 <= x - 1) and ([x-1, y] not in visited) and (arr[x-1][y] == 1 or arr[x-1][y] == 2 or arr[x-1][y] == 5 or arr[x-1][y] == 6):
            bfs.append([x - 1, y, arr[x-1][y]])
        
    
T = int(input())

for n in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    bfs = [[R, C, arr[R][C]]]
    for i in range(L):
        length = len(bfs)
        
        for j in range(length):
            if [bfs[j][0], bfs[j][1]] not in visited:
                visited.append([bfs[j][0], bfs[j][1]])
            center(bfs[j][0], bfs[j][1], bfs[j][2])

        for j in range(length):
            bfs.pop(0)

    print("#{0} {1}".format(n, len(visited)))