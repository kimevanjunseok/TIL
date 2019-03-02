def counter(n):
    global cnt, iron_water
    for i in range(5):
        for j in range(5):
            if iron_water[i][j] == n:
                iron_water[i][j] = 0

    count_3 = 0
    count_4 = 0
    for i in range(5):
        count_1 = 0
        count_2 = 0
        for j in range(5):
            
            if iron_water[i][j] == 0:
                count_1 += 1

            if iron_water[j][i] == 0:
                count_2 += 1

        if iron_water[i][i] == 0:
            count_3 += 1

        if iron_water[i][4-i] == 0:
            count_4 += 1

        if count_1 == 5:
            cnt += 1

        if count_2 == 5:
            cnt += 1

    if count_3 == 5:
        cnt += 1

    if count_4 == 5:
        cnt += 1

iron_water = [list(map(int, input().split())) for _ in range(5)]
arr = []

for i in range(5):
    arr += list(map(int, input().split()))
result = 0
for i in range(len(arr)):
    cnt = 0
    counter(arr[i])
    if cnt >= 3:
        result = i+1
        break
print(result)


