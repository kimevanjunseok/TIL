N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
x, y = 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            x = i
            y = j
max_num = 0
com = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            com = (x-i)**2 + (y-j)**2
            if max_num < com:
                max_num = com
L = list(map(lambda x:x**2, range(1, 14)))

print(int(max_num**0.5)) if max_num in L else print(int(max_num**0.5) + 1)