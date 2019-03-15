import sys
sys.stdin = open('등산로조성_input.txt')

def find_max():
    global arr, N
    max_num = 0

    for i in range(N):
        if max_num < max(arr[i]):
            max_num = max(arr[i])

    return [[i, j] for i in range(N) for j in range(N) if arr[i][j] == max_num]

def right(x, y):
    global max_road

    visited.append([x, y])

    if 0 <= y + 1 < N and arr[x][y] > arr[x][y + 1]:
        right(x, y + 1)

    if 0 <= y - 1 < N and arr[x][y] > arr[x][y - 1]:
        right(x, y - 1)

    if 0 <= x - 1 < N and arr[x][y] > arr[x - 1][y]:
        right(x - 1, y)

    if 0 <= x + 1 < N  and arr[x][y] > arr[x + 1][y]:
        right(x + 1, y)

    if len(visited) > max_road:
        max_road = len(visited)

    visited.pop()

T = int(input())

for n in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_road = 0
    location = find_max()
    for i in range(N):
        for j in range(N):
            for _ in range(K):
                arr[i][j] += -1
                for k in location:
                    visited = []
                    right(k[0], k[1])

            arr[i][j] += K

    print("#{0} {1}".format(n, max_road))
