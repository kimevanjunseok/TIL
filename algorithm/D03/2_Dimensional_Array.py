arr = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
# #행우선
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j], end = " ")
#     print()
# print()

#열우선
for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j], end = " ")
    print()
print()

# #지그재그 순회
# n = len(arr)
# m = len(arr[0])
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j+(m-1-2*j) * (i%2)], end = " ")
#     print()