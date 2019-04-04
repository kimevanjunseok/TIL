def dfs(x, y, z, score, star):
    global maxN, cnt
    if maxN == cnt*10:
        return
    if maxN >= score and star == 0:
        return
    if x == 0:
        if score > maxN:
            maxN = score
        return
    for i in range(3):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0 <= ax < 13 and 0 <= ay < 5 and [ax, ay] not in visited:
            if z - 5 < ax <= z:
                if arr[ax][ay] == "X" or arr[ax][ay] == "0":
                    visited.append([ax, ay])
                    dfs(ax, ay, z, score, star)
                    visited.pop()
                elif arr[ax][ay] == "*":
                    visited.append([ax, ay])
                    dfs(ax, ay, z, score+10, star-1)
                    visited.pop()

            else:
                if arr[ax][ay] == "X":
                    visited.append([ax, ay])
                    dfs(ax, ay, z, score-7, star)
                    visited.pop()
                elif arr[ax][ay] == "0":
                    visited.append([ax, ay])
                    dfs(ax, ay, z, score, star)
                    visited.pop()
                else:
                    visited.append([ax, ay])
                    dfs(ax, ay, z, score+10, star-1)
                    visited.pop()

T = int(input())
for n in range(T):
    arr = [list(input()) for _ in range(13)]
    dx = [-1, -1, -1]
    dy = [0, 1, -1]
    maxN = -7*13
    cnt = 0
    List = []
    for i in range(13):
        for j in range(5):
            if arr[i][j] == "*":
                cnt += 1

    for i in range(4, 12):
        visited = [[12, 2]]
        dfs(12, 2, i, 0, cnt)
        if maxN == cnt*10:
            break
    print(maxN)
