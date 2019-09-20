import sys
sys.stdin = open("그룹나누기_input.txt")

def DFS(n):
    global N

    visited[n] = False

    for i in range(1, N+1):
        if check[n][i] and visited[i]:
            DFS(i)
    return

T = int(input())

for n in range(1, T+1):
    N, M = map(int, input().split())
    board = list(map(int, input().split()))
    arr = [[board[i],board[i+1]] for i in range(0, len(board), 2)]
    check = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(len(arr)):
        check[arr[i][0]][arr[i][1]] = 1
        check[arr[i][1]][arr[i][0]] = 1
    visited = [True] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if visited[i]:
            cnt += 1
            DFS(i)

    print("#{} {}".format(n, cnt))
