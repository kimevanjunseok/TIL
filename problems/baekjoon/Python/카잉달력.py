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
    result = -1

    com_1 = set([i + x for i in range(0, lcm_num, M)])
    com_2 = set([i + y for i in range(0, lcm_num, N)])

    if com_1 & com_2:
        result = max(com_1 & com_2)


    print(result)

