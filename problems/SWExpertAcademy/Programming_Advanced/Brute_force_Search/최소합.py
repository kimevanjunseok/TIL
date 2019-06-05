import sys
sys.stdin = open("최소합_input.txt")

def DFS(x, y, sums):
    global N, minN
    if sums >= minN:
        return

    if x == N-1 and y == N-1:
        minN = sums
    else:
        for i in range(2):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < N and 0 <= ay < N:
                DFS(ax, ay, sums + arr[ax][ay])

T = int(input())

for n in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minN = 9999999999
    dx = [1, 0]
    dy = [0, 1]
    DFS(0, 0, arr[0][0])
    print("#{0} {1}".format(n, minN))
