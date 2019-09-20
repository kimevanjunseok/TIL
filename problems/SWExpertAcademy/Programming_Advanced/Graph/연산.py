import sys
sys.stdin = open("연산_input.txt")

def BFS(N):
    global M
    q = [[N, 0]]
    visited.append(N)
    cnt = 0
    while q:
        x, y = q[cnt]
        dv = [x+1, x-1, x*2, x-10]
        for i in range(4):
            if dv[i] == M:
                return y+1
            
            if 0 < dv[i] < 1000000 and visited[dv[i]]:
                q.append([dv[i], y+1])
                visited[dv[i]] = False
        cnt += 1

T = int(input())

for n in range(1, T+1):
    N, M = map(int, input().split())
    visited = [True] * (1000000)
    print("#{} {}".format(n, BFS(N)))