X, Y = map(int, input().split())
store = int(input())
arr = [list(map(int, input().split())) for _ in range(store)]
dong = list(map(int, input().split()))

cnt = 0


if dong[0] == 1:
    for i in range(len(arr)):
        if arr[i][0] == 1:
            cnt += (max(dong[1], arr[i][1]) - min(dong[1], arr[i][1]))

        elif arr[i][0] == 2:
            a = Y + dong[1] + arr[i][1]
            b = Y + (X-dong[1]) + (X-arr[i][1])
            if a > b:
                cnt += b
            else:
                cnt += a

        elif arr[i][0] == 3:
            cnt += (dong[1] + arr[i][1])

        elif arr[i][0] == 4:
            cnt += (X - dong[1] + arr[i][1])

elif dong[0] == 2:
    for i in range(len(arr)):
        if arr[i][0] == 2:
            cnt += (max(dong[1], arr[i][1]) - min(dong[1], arr[i][1]))

        elif arr[i][0] == 1:
            a = Y + dong[1] + arr[i][1]
            b = Y + (X-dong[1]) + (X-arr[i][1])
            if a > b:
                cnt += b
            else:
                cnt += a

        elif arr[i][0] == 3:
            cnt += (dong[1] + Y - arr[i][1])

        elif arr[i][0] == 4:
            cnt += (X - dong[1] + Y - arr[i][1])

elif dong[0] == 3:
    for i in range(len(arr)):
        if arr[i][0] == 3:
            cnt += (max(dong[1], arr[i][1]) - min(dong[1], arr[i][1]))

        elif arr[i][0] == 4:
            a = X + dong[1] + arr[i][1]
            b = X + (Y - dong[1]) + (Y - arr[i][1])
            if a > b:
                cnt += b
            else:
                cnt += a

        elif arr[i][0] == 1:
            cnt += (dong[1] + arr[i][1])

        elif arr[i][0] == 2:
            cnt += (Y - dong[1] + arr[i][1])

elif dong[0] == 4:
    for i in range(len(arr)):
        if arr[i][0] == 4:
            cnt += (max(dong[1], arr[i][1]) - min(dong[1], arr[i][1]))

        elif arr[i][0] == 3:
            a = X + dong[1] + arr[i][1]
            b = X + (Y - dong[1]) + (Y - arr[i][1])
            if a > b:
                cnt += b
            else:
                cnt += a

        elif arr[i][0] == 1:
            cnt += (dong[1] + X - arr[i][1])

        elif arr[i][0] == 2:
            cnt += (Y - dong[1] + X - arr[i][1])

print(cnt)