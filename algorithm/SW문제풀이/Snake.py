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

time = 0
head = [[1, 1]]
index = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while True:

    if time == int(arr[0][0]):
        v1 = arr.pop(0)
        if v1[1] == "D":
            index += 1
            if index == 4:
                index = 0
        elif v1[1] == "L":
            index += -1
            if index == -1:
                index = 3
    time += 1
    head.append([head[-1][0]+dy[index], head[-1][1]+dx[index]])

    if time == 1:
        head.pop(0)

    if space[head[-1][0]][head[-1][1]] == 9:
        break

    elif space[head[-1][0]][head[-1][1]] == 1:
        space[head[-1][0]][head[-1][1]] = 9

    else:
        space[head[-1][0]][head[-1][1]] = 9
        if time > 1:
            v2 = head.pop(0)
            space[v2[0]][v2[1]] = 0

    Printlocation()
    print()


print(time)
