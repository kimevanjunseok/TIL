T = int(input())

for n in range(T):
    N, K_Min, K_Max = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    arr_set_list = sorted(list(set(arr)))
    result = 9999999
    for i in range(len(arr_set_list)-1):
        for j in range(i+1, len(arr_set_list)):
            cnt_1 = 0
            cnt_2 = 0
            cnt_3 = 0
            for k in range(len(arr)):
                if arr[k] < arr_set_list[i]:
                    cnt_1 += 1
                elif arr_set_list[i] <= arr[k] < arr_set_list[j]:
                    cnt_2 += 1
                elif arr_set_list[j] <= arr[k]:
                    cnt_3 += 1

            if (K_Min <= cnt_1 <= K_Max) and (K_Min <= cnt_2 <= K_Max) and (K_Min <= cnt_3 <= K_Max):
                if result > max(cnt_1, cnt_2, cnt_3) - min(cnt_1, cnt_2, cnt_3):
                    result = max(cnt_1, cnt_2, cnt_3) - min(cnt_1, cnt_2, cnt_3)

    print(-1) if result == 9999999 else print(result)




