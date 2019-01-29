import sys
sys.stdin = open("회문2_input.txt")

T = 10
for i in range(1, T+1):
    arr = []
    max_result = 1
    N = int(input())
    for j in range(100):
        arr.append(input())

    for M in range(2, 101):
        for j in range(100):
            cnt = 0
            cnt_test = 0
            result1 = ""
            while True:
                if cnt == 100 - M + 1:
                    break

                if arr[j][cnt] == arr[j][cnt + M - cnt_test - 1]:
                    if M - cnt_test - 1 < 2:
                        result1 = arr[j][(cnt + M - cnt_test - 1 - M // 2):(cnt + 2 * M - cnt_test - M // 2 -1)]
                        if max_result < len(result1):
                            max_result = len(result1)
                    cnt += 1
                    cnt_test += 2

                else:
                    cnt = cnt - cnt_test // 2 + 1
                    cnt_test = 0


    for M in range(2, 101):
        for j in range(100):
            cnt = 0
            cnt_test = 0
            while True:
                if cnt == 100 - M + 1:
                    break

                if arr[cnt][j] == arr[cnt + M - cnt_test -1][j]:
                    if M - cnt_test - 1 < 2:
                        result2 = ""
                        for k in range((cnt + M - cnt_test - 1 - M // 2), (cnt + 2 * M - cnt_test - M // 2 -1)):
                            result2 += arr[k][j]
                        if max_result < len(result2):
                            max_result = len(result2)
                            # print(result2)
                    cnt += 1
                    cnt_test += 2

                else:
                    cnt = cnt - cnt_test // 2 + 1
                    cnt_test = 0

    print(f"#{i} {max_result}")