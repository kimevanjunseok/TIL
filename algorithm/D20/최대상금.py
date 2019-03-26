import sys
sys.stdin = open('최대상금_input.txt')

def change(x):
    global N, arr, result

    if x > N:
        int_num = int("".join(arr))
        if result < int_num:
            result = int_num
        return

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            change(x+1)
            arr[i], arr[j] = arr[j], arr[i]

T = int(input())

for n in range(1, T+1):
    arr, N = input().split()
    N = int(N)
    arr = list(arr)
    result = 0
    if len(arr) > N:
        change(1)

    else:
        cnt = 0
        while True:
            if arr[cnt] < max(arr[cnt + 1:]):
                L = arr[cnt + 1:]
                arr[cnt], arr[len(arr) - arr[::-1].index(max(L)) - 1] = arr[len(arr) - arr[::-1].index(max(L)) - 1], arr[cnt]
                N += -1

            cnt += 1

            if cnt == len(arr) - 1:
                N = N%len(arr)
                break

        change(1)

    print('#{0} {1}'.format(n, result))
