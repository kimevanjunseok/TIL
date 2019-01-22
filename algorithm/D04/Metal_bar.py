import sys
sys.stdin = open("Metal_bar_input.txt")

T = int(input())

for i in range(1, T+1):
    N = int(input())
    test = list(map(int, input().split()))
    arr = [[0 for _ in range(2)] for _ in range(N)]
    num = 0

    for j in range(N):
        for k in range(2):
            arr[j][k] = test[num]
            num += 1

    cnt = 1
    result = arr[:1]

    while cnt != N:

        if result[-1][1] == arr[cnt][0]:
            result += [arr[cnt]]
            cnt = 0

        if result[0][0] == arr[cnt][1]:
            result = [arr[cnt]] + result
            cnt = 0
        cnt += 1

    result1 = ""

    for j in result:
        for k in j:
            k = str(k)
            result1 += k + ' '

    print(f"#{i} {result1.rstrip()}")