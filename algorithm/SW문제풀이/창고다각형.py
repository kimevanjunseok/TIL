N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

area = 0

if N == 1:
    area = arr[0][1]

elif N == 2:
    arr.sort()
    h = []
    for i in arr:
        h.append(i[1])
    max_h = max(h)
    min_h = min(h)
    area = (max_h) + (min_h * (arr[1][0] - arr[0][0]))

else:
    arr.sort()

    h = []
    for i in arr:
        h.append(i[1])
    max_h = max(h)

    
    index = 1
    height_1 = arr[0][1]
    width_1 = arr[0][0]
    while True:
        if height_1 < arr[index][1]:
            area += (height_1 * (arr[index][0] - width_1))
            height_1 = arr[index][1]
            width_1 = arr[index][0]
        if height_1 == max_h:
            break
        index += 1

    index = len(arr) - 2
    height_2 = arr[len(arr)-1][1]
    width_2 = arr[len(arr)-1][0]

    while True:
        if height_2 < arr[index][1]:
            area += (height_2 * (width_2 - arr[index][0]))
            height_2 = arr[index][1]
            width_2 = arr[index][0]
        if height_2 == max_h:
            break
        index += -1

    area += max_h * (width_2 - width_1 + 1)
    
print(area)