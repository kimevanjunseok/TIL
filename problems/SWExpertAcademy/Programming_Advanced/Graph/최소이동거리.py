import sys
sys.stdin = open("최소이동거리_input.txt")

T = int(input())

for n in range(1, T+1):
    N, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    p = [99999999] * (N+1)
    p[0] = 0
    for i in range(len(arr)):
        if arr[i][2] + p[arr[i][0]] < p[arr[i][1]]:
            p[arr[i][1]] = arr[i][2] + p[arr[i][0]]
    print("#{} {}".format(n, p[-1]))