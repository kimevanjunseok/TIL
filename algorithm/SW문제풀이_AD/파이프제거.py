N = int(input())
Y, X = map(int, input().split())
arr = [list(input()) for _ in range(N)]
q = [[X, Y, arr[X][Y]]]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
arr[X][Y] = "0"
while q:
    x, y, num = q.pop(0)
    for i in range(4):
        if i == 0:
            if num in ["1", "3", "6", "7", "8", "A", "B"]:
                if 0 <= y + dy[i] < N and arr[x + dx[i]][y + dy[i]] in ["1", "4", "5", "8", "9", "A", "B"]:
                    q.append([x + dx[i], y + dy[i], arr[x + dx[i]][y + dy[i]]])
                    arr[x + dx[i]][y + dy[i]] = "0"
        elif i == 1:
            if num in ["1", "4", "5", "8", "9", "A", "B"]:
                if 0 <= y + dy[i] < N and arr[x + dx[i]][y + dy[i]] in ["1", "3", "6", "7", "8", "A", "B"]:
                    q.append([x + dx[i], y + dy[i], arr[x + dx[i]][y + dy[i]]])
                    arr[x + dx[i]][y + dy[i]] = "0"
        elif i == 2:
            if num in ["2", "5", "6", "7", "9", "A", "B"]:
                if 0 <= x + dx[i] < N and arr[x + dx[i]][y + dy[i]] in ["2", "3", "4", "7", "8", "9", "B"]:
                    q.append([x + dx[i], y + dy[i], arr[x + dx[i]][y + dy[i]]])
                    arr[x + dx[i]][y + dy[i]] = "0"
        elif i == 3:
            if num in ["2", "3", "4", "7", "8", "9", "B"]:
                if 0 <= x + dx[i] < N and arr[x + dx[i]][y + dy[i]] in ["2", "5", "6", "7", "9", "A", "B"]:
                    q.append([x + dx[i], y + dy[i], arr[x + dx[i]][y + dy[i]]])
                    arr[x + dx[i]][y + dy[i]] = "0"
cnt = 0                  
for i in arr:
    cnt += i.count("0")
print(N*N - cnt)

