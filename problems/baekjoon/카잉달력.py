N = int(input())

def gcd(x, y):
    a = max(x, y)
    b = min(x, y)
    while True:
        a, b = b, a % b
        if b == 0:
            return a

def lcm(x, y):
    a = gcd(x, y)
    return (x*y) // a

for n in range(N):
    M, N, x, y = map(int, input().split())
    gcd_num = gcd(M, N)
    lcm_num = lcm(M, N)
    stack = []
    result = 0
    for i in range(M, lcm_num+1, M):
        print(i)
        if (i+x) % N == y:
            result = i+x
            break
    print(result) if result else print(-1)

