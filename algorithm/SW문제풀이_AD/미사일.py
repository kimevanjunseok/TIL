def remove():
    global M, B, D

    for i in range(M):
        if t[i][2] > 0:
            t[i][2] += -B
            for j in range(len(arr)):
                if t[i] != arr[j] and abs(t[i][0] - arr[j][0]) + abs(t[i][1] - arr[j][1]) <= D:
                    arr[j][2] += -B

def finder():
    global minN
    cnt = 0
    for i in range(len(arr)):
        if arr[i][2] > 0:
            cnt += 1
    if minN > cnt:
        minN = cnt

def combi(x, y):
    global N
    if y == 0:
        remove()
        finder()
        for i in range(N):
            arr[i][2] = copy[i]

    elif x == 0:
        return
    else:
        t[y-1] = arr[x-1]
        combi(x, y-1)
        combi(x-1, y)

N =int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M, B, D = map(int, input().split())
minN = 9999999999999
t = [0] * M
copy = [0] * N
for i in range(N):
    copy[i] = arr[i][2]
combi(N, M)
print(minN)

#################################################################################
# def clear(no):
#     global N, R, P
#     for i in range(N):
#         temp = abs(arr[no][0] - arr[i][0]) + abs(arr[no][1] - arr[i][1])
#         if temp <= R:
#             arr[i][2] += -P
#
# def update(no):
#     global N, R, P
#     for i in range(N):
#         temp = abs(arr[no][0] - arr[i][0]) + abs(arr[no][1] - arr[i][1])
#         if temp <= R:
#             arr[i][2] += P
#
# def DFS(no):
#     global sol, M
#     if no == M:
#         cnt = 0
#         for i in range(N):
#             if arr[i][2] > 0: cnt += 1
#         if cnt < sol: sol = cnt
#         return
#     for i in range(N):
#         if arr[i][2] <= 0: continue
#         clear(i)
#         DFS(no+1)
#         update(i)
#
# N = int(input())
# arr = []
# for i in range(N):
#     arr.append(list(map(int, input().split())))
# M, P, R = map(int, input().split())
# sol = 16
# DFS(0)
# print(sol)
