def judge(x, y):

    global arr, N

    apple_1 = []
    apple_2 = []
    apple_3 = []
    apple_4 = []

    result_1 = 0
    apple_1 = [[arr[i][j] for j in range(y)] for i in range(x)]
    for i in range(len(apple_1)):
        result_1 += apple_1[i].count(1)

    result_2 = 0
    apple_2 = [[arr[i][j] for j in range(y, N)] for i in range(x)]
    for i in range(len(apple_2)):
        result_2 += apple_2[i].count(1)

    result_3 = 0
    apple_3 = [[arr[i][j] for j in range(y)] for i in range(x, N)]
    for i in range(len(apple_3)):
        result_3 += apple_3[i].count(1)

    result_4 = 0
    apple_4 = [[arr[i][j] for j in range(y, N)] for i in range(x, N)]
    for i in range(len(apple_4)):
        result_4 += apple_4[i].count(1)

    if result_1 == result_2 == result_3 == result_4:
        return True
    return False

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
cnt = 0
for i in range(1, N):
    for j in range(1, N):
        if judge(i,j):
            cnt += 1

print(cnt) if cnt else print(-1)