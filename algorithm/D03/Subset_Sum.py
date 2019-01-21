#bit = [0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             print(bit)

arr = [1,2,4]
n = len(arr)
for i in range(1<<n):
    print(f"i 는 {i}")
    for j in range(n+1):
        print(f"j 는 {j}")
        print(1<<j)
        print(f"{i & (1<<j)}")
        if i & (1<<j):
            print(f"이건 답{arr[j]}", end=", ")
    print()
print()

# arr = [-7, -3, -2, 5, 7]
# n = len(arr)
# cnt = 0
# for i in range(1<<n):
#     L = []
#     for j in range(n+1):
#         if i & (1<<j):
#             L.append(arr[j])
#     if sum(L) == 0:
#         cnt +=1
# print(cnt-1)