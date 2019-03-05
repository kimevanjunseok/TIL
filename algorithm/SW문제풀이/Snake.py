def Printlocation():
    global space

    for i in space:
        for j in i:
            print(j, end=" ")
        print()


N = int(input())
K = int(input())
Apple_location = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
arr = [input().split() for _ in range(L)]

space = [[9]*(N+2)] + [[9] + [0 for _ in range(N)] + [9] for _ in range(N)] + [[9]*(N+2)]
for i in Apple_location:
    space[i[0]][i[1]] = 1

snake = [[1, 2] ,[1, 1]]
time = 0
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
index = 0
while True:

    time += 1

    if int(arr[0][0]) == time:
        v = arr.pop()
        if v[1] == "D":
            index += 1
            if index > 3:
                index = 0
        if v[1] == "L":
            index += -1
            if index < 0:
                index = 3

    for i in snake:
        space[i[0]][i[1]] = 9
    
    for i in snake:
        i[0] += dx[index] 
        i[1] += dy[index]

    if space[snake[0][0]][snake[0][1]] == 1:
        snake += [snake[-1][0] - dx[index], snake[-1][1] - dy[index]]
    if space[snake[0][0]][snake[0][1]] == 9:
        break
    
    Printlocation()
    print()