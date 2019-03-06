N = int(input())
arr = [[1]*(N+2)] + [[1] + list(map(int, list(input()))) + [1] for _ in range(N)] + [[1]*(N+2)]
finder = list(map(int, input().split()))
head = [[1,1]]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
cnt = 0
num = 0
while True:
    v = finder[num]

    if v == 1:
        index = 0
    elif v == 2:
        index = 1
    elif v == 3:
        index = 2
    elif v == 4:
        index = 3

    while True:
        if arr[head[-1][0]+dx[index]][head[-1][1]+dy[index]] == 1:
            break

        arr[head[-1][0]][head[-1][1]] = 1
        head.append([head[-1][0] + dx[index], head[-1][1] + dy[index]])

        cnt += 1

    if [head[-1][0]+dx[index], head[-1][1]+dy[index]] in head:
        break

    num += 1

    if num == len(finder):
        num = 0

print(cnt)