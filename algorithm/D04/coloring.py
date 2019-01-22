import sys
sys.stdin = open("coloring_input.txt")

T = int(input())

for i in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)]
    result = 0
    for j in range(N):
        arr_color = list(map(int, input().split()))
        for a in range(arr_color[0], arr_color[2]+1):
            for b in range(arr_color[1], arr_color[3]+1):
                arr[a][b] += arr_color[4]

    for j in range(10):
        for k in range(10):
            if arr[j][k] >= 3:
                result += 1

    print(f"#{i} {result}")

