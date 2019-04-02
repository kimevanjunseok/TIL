import sys
sys.stdin = open("연산_input.txt")

T = int(input())

for n in range(1, T+1):
    N, M = map(int, input().split())
    v = [0 for _ in range(1000000+1)]
    v[N] = 1
    q = [N]
    result = 0
    cnt = 0
    while q:
        x = q[cnt]
        dx = [x+1, x-1, x*2, x-10]
        for i in range(4):
            if dx[i] == M:
                result = v[x]
                break
            if 0 < dx[i] <= 1000000 and v[dx[i]] == 0:
                v[dx[i]] = v[x] +1
                q.append(dx[i])
        if result:
            break
        cnt += 1

    print("#{0} {1}".format(n, result))




