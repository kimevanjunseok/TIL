import sys
sys.stdin = open("snail_number_input.txt")

T = int(input())

for N in range(1, T+1):
    Number = int(input())
    for M in range(N):
        arr = [[0 for _ in range(Number)] for _ in range(Number)]
        L = list(range(1, Number * Number+1))
        cnt = 0
        point = 0

        while cnt != Number*Number:
            for i in range(Number-cnt*2):
                arr[cnt][i+cnt] = L[point]
                point += 1

            for i in range(1, Number-cnt*2):
                arr[i+cnt][Number-1-cnt] = L[point]
                point += 1


            for i in range(1, Number-cnt*2):
                arr[Number-1-cnt][Number-1-cnt-i] = L[point]
                point += 1

            for i in range(1, Number-1-cnt*2):
                arr[Number-1-cnt-i][cnt] = L[point]
                point += 1

            cnt += 1
    print(f"#{N}")
    for i in range(Number):
        for j in range(Number):
            print(arr[i][j], end=' ')
        print()