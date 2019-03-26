import sys
sys.stdin = open('최소합_input.txt')

def right(x, y, sums):
    global N, minN

    sums += arr[x][y]

    if x == N-1 and y == N-1:
        if sums < minN:
            minN = sums
        return

    if x+1 < N:
        right(x+1, y, sums)
    if y+1 < N:
        right(x, y+1, sums)

T = int(input())

for n in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minN = 999999999999999999999999
    right(0, 1, arr[0][0])
    right(1, 0, arr[0][0])
    print('#{0} {1}'.format(n, minN))
