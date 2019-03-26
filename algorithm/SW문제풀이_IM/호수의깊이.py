N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            cnt_1 = 0
            while True:
                cnt_1 += 1
                if arr[i+cnt_1][j] == 0:
                    break
            cnt_2 = 0
            while True:
                cnt_2 += 1
                if arr[i-cnt_2][j] == 0:
                    break
            cnt_3 = 0
            while True:
                cnt_3 += 1
                if arr[i][j+cnt_3] == 0:
                    break
            cnt_4 = 0
            while True:
                cnt_4 += 1
                if arr[i][j-cnt_4] == 0:
                    break
            arr[i][j] = min(cnt_1, cnt_2, cnt_3, cnt_4)
result = 0
for i in range(N):
    for j in range(N):
        result += arr[i][j]
print(result)
