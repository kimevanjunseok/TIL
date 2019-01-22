import sys
sys.stdin = open("SUM.txt")

T = 10
for N in range(1, T+1):
    Num = int(input())
    arr = [[0 for _ in range(100)] for _ in range(100)]
    max_sum = 0

    for i in range(100):
        arr[i] = list(map(int, input().split()))

    for i in range(100):
        com_sum = 0
        for j in range(100):
            com_sum += arr[i][j]
        if max_sum < com_sum:
            max_sum = com_sum

    for i in range(100):
        com_sum = 0
        for j in range(100):
            com_sum += arr[j][i]
        if max_sum < com_sum:
            max_sum = com_sum

    com_sum = 0
    for i in range(100):
        com_sum += arr[i][i]
        if max_sum < com_sum:
            max_sum = com_sum

    com_sum = 0
    for i in range(100):
        com_sum += arr[i][99-i]
        if max_sum < com_sum:
            max_sum = com_sum

    print(f"#{N} {max_sum}")