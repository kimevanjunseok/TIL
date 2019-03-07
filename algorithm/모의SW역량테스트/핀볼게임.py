import sys
sys.stdin = open('핀볼게임_input.txt')

def finder(x, y, z):
    global N
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == z:
                if x != i or y != j:
                    return [i, j]

T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for n in range(1, T+1):
    N = int(input())
    arr = [[5] * (N+2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5] * (N+2)]
    result = 0
    visited = []
    cnt = 0
    count = 0
    S = ['right', 'left', 'up', 'down']
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 0:
                visited.append([i, j])
                for k in S:
                    String = k
                    x = i
                    y = j
                    while True:
                        if String == 'right':
                            count += 1

                            while True:
                                x += dx[0]
                                y += dy[0]
                                if count > 1:
                                    if [x, y] in visited:
                                        break
                                if arr[x][y] != 0:
                                    break
                            if arr[x][y] == 0:
                                if result < cnt:
                                    result = cnt
                                cnt = 0
                                count = 0
                                break
                            elif arr[x][y] == 1 or arr[x][y] == 2 or arr[x][y] == 5:
                                cnt += 1
                                String = 'left'
                            elif arr[x][y] == 3:
                                cnt += 1
                                String = 'down'
                            elif arr[x][y] == 4:
                                cnt += 1
                                String = 'up'
                            elif 6 <= arr[x][y] <= 10:
                                head = finder(x, y, arr[x][y])
                                x = head[0]
                                y = head[1]
                                String = 'right'
                            elif arr[x][y] == -1:
                                if result < cnt:
                                    result = cnt
                                cnt = 0
                                count = 0
                                break

                        elif String == 'left':
                            count += 1
                            while True:
                                x += dx[1]
                                y += dy[1]
                                if count > 1:
                                    if [x, y] in visited:
                                        break
                                if arr[x][y] != 0:
                                    break
                            if arr[x][y] == 0:
                                if result < cnt:
                                    result = cnt
                                cnt = 0
                                count = 0
                                break
                            elif arr[x][y] == 3 or arr[x][y] == 4 or arr[x][y] == 5:
                                cnt += 1
                                String = 'right'
                            elif arr[x][y] == 2:
                                cnt += 1
                                String = 'down'
                            elif arr[x][y] == 1:
                                cnt += 1
                                String = 'up'
                            elif 6 <= arr[x][y] <= 10:
                                head = finder(x, y, arr[x][y])
                                x = head[0]
                                y = head[1]
                                String = 'left'
                            elif arr[x][y] == -1:
                                if result < cnt:
                                    result = cnt
                                cnt = 0
                                count = 0
                                break
                        elif String == 'up':
                            count += 1
                            while True:
                                x += dx[2]
                                y += dy[2]
                                if count > 1:
                                    if [x, y] in visited:
                                        break
                                if arr[x][y] != 0:
                                    break
                            if arr[x][y] == 0:
                                if result < cnt:
                                    result = cnt
                                cnt = 0
                                count = 0
                                break
                            elif arr[x][y] == 1 or arr[x][y] == 4 or arr[x][y] == 5:
                                cnt += 1
                                String = 'down'
                            elif arr[x][y] == 2:
                                cnt += 1
                                String = 'right'
                            elif arr[x][y] == 3:
                                cnt += 1
                                String = 'left'
                            elif 6 <= arr[x][y] <= 10:
                                head = finder(x, y, arr[x][y])
                                x = head[0]
                                y = head[1]
                                String = 'up'
                            elif arr[x][y] == -1:
                                if result < cnt:
                                    result = cnt
                                cnt = 0
                                count = 0
                                break
                        elif String == 'down':
                            count += 1
                            while True:
                                x += dx[3]
                                y += dy[3]
                                if count > 1:
                                    if [x, y] in visited:
                                        break
                                if arr[x][y] != 0:
                                    break
                            if arr[x][y] == 0:
                                if result < cnt:
                                    result = cnt
                                cnt = 0
                                count = 0
                                break
                            elif arr[x][y] == 2 or arr[x][y] == 3 or arr[x][y] == 5:
                                cnt += 1
                                String = 'up'
                            elif arr[x][y] == 1:
                                cnt += 1
                                String = 'right'
                            elif arr[x][y] == 4:
                                cnt += 1
                                String = 'left'
                            elif 6 <= arr[x][y] <= 10:
                                head = finder(x, y, arr[x][y])
                                x = head[0]
                                y = head[1]
                                String = 'down'
                            elif arr[x][y] == -1:
                                if result < cnt:
                                    result = cnt
                                cnt = 0
                                count = 0
                                break

                visited.pop()
    print("#{0} {1}".format(n, result))