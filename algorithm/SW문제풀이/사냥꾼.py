N = int(input())
arr = [[0]*(N+2)] + [[0] + list(map(int, list(input()))) + [0] for _ in range(N)] + [[0]*(N+2)]

stack = []

location = []

def one(x, y):
    while True:
        x += -1
        if arr[x][y] == 0:
            break
        elif arr[x][y] == 2:
            if [x, y] not in stack:
                stack.append([x, y])
def two(x, y):
    while True:
        x += -1
        y += 1
        if arr[x][y] == 0:
            break
        elif arr[x][y] == 2:
            if [x, y] not in stack:
                stack.append([x, y])
def three(x, y):
    while True:
        y += 1
        if arr[x][y] == 0:
            break
        elif arr[x][y] == 2:
            if [x, y] not in stack:
                stack.append([x, y])
def four(x, y):
    while True:
        x += 1
        y += 1
        if arr[x][y] == 0:
            break
        elif arr[x][y] == 2:
            if [x, y] not in stack:
                stack.append([x, y])
def five(x, y):
    while True:
        x += 1
        if arr[x][y] == 0:
            break
        elif arr[x][y] == 2:
            if [x, y] not in stack:
                stack.append([x, y])
def six(x, y):
    while True:
        x += 1
        y += -1
        if arr[x][y] == 0:
            break
        elif arr[x][y] == 2:
            if [x, y] not in stack:
                stack.append([x, y])
def seven(x, y):
    while True:
        y += -1
        if arr[x][y] == 0:
            break
        elif arr[x][y] == 2:
            if [x, y] not in stack:
                stack.append([x, y])
def eight(x, y):
    while True:
        x += -1
        y += -1
        if arr[x][y] == 0:
            break
        elif arr[x][y] == 2:
            if [x, y] not in stack:
                stack.append([x, y])
for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j] == 1:
            location.append([i, j])

for i in location:
    one(i[0], i[1])
    two(i[0], i[1])
    three(i[0], i[1])
    four(i[0], i[1])
    five(i[0], i[1])
    six(i[0], i[1])
    seven(i[0], i[1])
    eight(i[0], i[1])
print(len(stack))


