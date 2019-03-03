# N = int(input())
# arr = [int(input()) for _ in range(N)]
# arr.sort()
# result = 0
# print(arr)
# for i in range(len(arr)-2):
#     for j in range(i+1, len(arr)-1):
#         cnt = j + 1
#         if 2*(arr[j] - arr[i]) < (arr[j+1] - arr[j]): 
#             break
#         elif (arr[cnt] - arr[j]) < (arr[j] - arr[i]):
#             while cnt != len(arr)-1:
#                 cnt += 1
#                 if (arr[cnt] - arr[j]) >= (arr[j] - arr[i]):
#                     break

#             while cnt != len(arr):
#                 if 2*(arr[j] - arr[i]) < (arr[cnt] - arr[j]) or (arr[cnt] - arr[j]) < (arr[j] - arr[i]):
#                     break
#                 else:
#                     print(arr[i], arr[j], arr[cnt])
#                     result += 1
#                     cnt += 1
#         else:
#             while cnt != len(arr):
#                 if 2*(arr[j] - arr[i]) < (arr[cnt] - arr[j]):
#                     break
#                 else:
#                     print(arr[i], arr[j], arr[cnt])
#                     result += 1
#                     cnt += 1

# print(result)

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
result = 0
for i in range(len(arr)-2):
    for j in range(len(arr)-1):
        time_2 = arr[j] + ((arr[j] - arr[i])*2)
        time_1 = arr[j] + (arr[j] - arr[i])
        length = time_2 - time_1 + 1
        result = (length - len(set(range(1)) - set(arr)))
print(result)
    
