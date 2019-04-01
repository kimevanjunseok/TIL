import sys
sys.stdin = open('최소이동거리_input.txt')

T = int(input())

for n in range(1, T+1):
    N, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    D = [0] * (N+1)
    board = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in arr:
        board[i[0]][i[1]] = i[2]

    for i in range(N+1):
        if arr[i][0] == 0:
            D[arr[i][1]] = arr[i][2]

    cnt = 1

    while cnt != N + 1:
        save = []
        for i in range(E):
            if arr[i][0] == cnt:
                if D[arr[i][1]] == 0:
                    D[arr[i][1]] = D[cnt] + board[cnt][arr[i][1]]
                else:
                    if D[arr[i][1]] > D[cnt] + board[cnt][arr[i][1]]:
                        D[arr[i][1]] = D[cnt] + board[cnt][arr[i][1]]

        cnt += 1
    print("#{0} {1}".format(n, D[-1]))