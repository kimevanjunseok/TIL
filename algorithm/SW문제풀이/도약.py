def bin_search_1(x, y):

    global arr

    if arr[y+1] - arr[y] >= arr[y] - arr[x]:
        return y + 1

    start = y + 1
    end = len(arr) - 1

    if start == end:
        return y + 1

    while start <= end:
        z = (start + end) // 2
        if arr[z] - arr[y] < arr[y] - arr[x]:
            start = z + 1
        else:
            if arr[z - 1] - arr[y] < arr[y] - arr[x] and arr[z] - arr[y] >= arr[y] - arr[x]:
                return z
            else:
                end = z - 1

# def bin_search_2(x, y):
#
#     global arr
#
#     if arr[y+1] - arr[y] > (arr[y] - arr[x])*2:
#         return y + 1
#
#     start = y + 1
#     end = len(arr) - 1
#
#     if start == end:
#         return y + 1
#
#
#     while start <= end:
#         z = (start + end) // 2
#         if arr[z-1] - arr[y] <= (arr[y] - arr[x])*2 and arr[z] - arr[y] > (arr[y] - arr[x])*2:
#             return z
#         elif arr[z] - arr[y] <= (arr[y] - arr[x])*2:
#             start = z+1
#         else:
#             end = z-1
#     return y+1

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
result = 0
max_max = max(arr)
for i in range(len(arr) - 2):
    for j in range(i + 1, len(arr) - 1):
        if arr[j] - arr[i] > max_max - arr[j]:
            break

        for k in range(bin_search_1(i, j), len(arr)):
            if arr[k] - arr[j] > (arr[j] - arr[i]) * 2:
                break

            if arr[j] - arr[i] <= arr[k] - arr[j] <= (arr[j] - arr[i]) * 2:
                result += 1

print(result)