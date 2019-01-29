import sys
sys.stdin = open("회문_input.txt")

T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    result = ""
    for j in range(N):
        arr.append(input())

    for j in range(N):
        cnt = 0
        cnt_test = 0
        while True:
            if arr[j][cnt] == arr[j][cnt + M - cnt_test -1]:
                if M - cnt_test -1 < 2:
                    result = arr[j][(cnt + M - cnt_test -1 - M // 2):(cnt + 2*M - cnt_test - M // 2)]
                    break
                cnt += 1
                cnt_test += 2

            else:
                cnt = cnt - cnt_test // 2 + 1
                cnt_test = 0
                if cnt == N - M + 1:
                    break
    if not result:
        for j in range(N):
            cnt = 0
            cnt_test = 0
            while True:
                if arr[cnt][j] == arr[cnt + M - cnt_test -1][j]:
                    if M - cnt_test -1 < 2:
                        for k in range((cnt + M - cnt_test -1 - M // 2), (cnt + 2*M - cnt_test - M // 2) -1):
                            result += arr[k][j]
                        break
                    cnt += 1
                    cnt_test += 2

                else:
                    cnt = cnt - cnt_test // 2 + 1
                    cnt_test = 0
                    if cnt == N - M + 1:
                        break

    print(f"#{i} {result}")