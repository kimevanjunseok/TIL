import sys
sys.stdin = open("화물도크_input.txt")

T = int(input())

for n in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x:x[1])
    cnt = 1
    com = arr[0][1]
    for i in range(1, N):
        if com <= arr[i][0]:
            com = arr[i][1]
            cnt += 1

    print("#{0} {1}".format(n, cnt))