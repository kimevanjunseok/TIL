N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
# arr = arr + arr[:k-1]
# first = arr[0]
# max_max = len(set(arr[:k]+[c]))
# for i in range(1, N):
#     if first != arr[i+1]:
#         first = arr[i+1]
#         if max_max < len(set(arr[i:i+k]+[c])):
#             max_max = len(set(arr[i:i+k]+[c]))
# print(max_max)
print(max([len(set(arr[i:i+k]+[c])) for i in range(N)]))
