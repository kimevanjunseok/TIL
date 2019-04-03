def finder1(x, y):
    for i in arr:
        if i[0] != x and i[1] != y:
            if abs(i[0] - x) + abs(i[1] - y) <= b[2]:
                arr[i[0]][i[1]] += -b[1]

def finder2(x, y):
    for i in arr:
        if i[0] != x and i[1] != y:
            if abs(i[0] - x) + abs(i[1] - y) <= b[2]:
                arr[i[0]][i[1]] += b[1]

def combi(x, y):
    global N, minN
    if y == 0:
        cnt = 0
        for i in range(len(t)):
            for j in range(len(arr)):
                if arr[j][0] == t[i][0] and arr[j][1] == t[i][1]:
                    arr[j][2] += -b[1]
                    finder1(t[i][0], t[i][1])

        for i in range(len(arr)):
            if arr[i][2] > 0:
                cnt += 1

        if cnt < minN:
            minN = cnt

        for i in range(len(t)):
            for j in range(len(arr)):
                if arr[j][0] == t[i][0] and arr[j][1] == t[i][1]:
                    arr[j][2] += b[1]
                    finder2(t[i][0], t[i][1])

    elif x == 0:
        return
    else:
        t[y-1] = arr[x-1]
        combi(x, y-1)
        combi(x-1, y)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
b = list(map(int, input().split()))
# map = [[0 for _ in range(1001)] for _ in range(1001)]
# for i in arr:
#     map[i[0]][i[1]] = i[2]


t = [0] * b[0]
minN = N
combi(N, b[0])
print(minN)

#
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
