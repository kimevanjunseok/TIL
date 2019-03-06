Y, X = map(int, input().split())
arr = [[1]*(X+2)] + [[1] + list(map(int, list(input()))) + [1] for i in range(Y)] + [[1]*(X+2)]
N = int(input())
List = list(map(int, input().split()))

x, y = 0, 0
for i in range(1, Y):
    for j in range(1, X):
        if arr[i][j] == 2:
            x = j
            y = i
            break

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
index = 0
stack = [[y, x]]
while List:
    v = List.pop(0)
    if v == 1:
        index = 0
    elif v == 2:
        index = 1
    elif v == 3:
        index = 2
    elif v == 4:
        index = 3

    while True:
        if arr[y + dy[index]][x + dx[index]] == 1:
            break
        x += dx[index]
        y += dy[index]
        if [y, x] not in stack:
            stack.append([y, x])

print(len(stack))
