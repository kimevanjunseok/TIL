N = int(input())
arr = list(map(int, input().split()))
max_num = 0

if N == 1:
    print(2)
else:
    first = arr[0]
    cnt_1 = 1
    for i in range(1, len(arr)):
        if first <= arr[i]:
            cnt_1 += 1
        else:
            cnt_1 = 1

        if max_num < cnt_1:
                max_num = cnt_1    
        first = arr[i]

    first = arr[0]
    cnt_1 = 1
    for i in range(1, len(arr)):
        if first >= arr[i]:
            cnt_1 += 1
        else:
            cnt_1 = 1
        if max_num < cnt_1:
                max_num = cnt_1    
        first = arr[i]

    print(max_num)