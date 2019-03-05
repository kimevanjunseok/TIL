import sys
sys.stdin = open("노드의합_input.txt")

def Treemake():
    global make, tree

    for i in range(1, N + 1):
        tree[i][0] = i

        if make:
            tree[i][1] = make.pop(0)

        if make:
            tree[i][2] = make.pop(0)


T = int(input())

for n in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    tree = [[0, 0, 0] for _ in range(N+1)]
    make = list(range(2, N+1))

    Treemake()

    result = [0] * (N+1)
    start = tree[-1][0]

    for i in arr:
        result[i[0]] = i[1]

    while True:
        for i in tree[::-1]:
            if result[i[1]] or result[i[2]]:
                if not result[i[0]]:
                    result[i[0]] = result[i[1]] + result[i[2]]
                    break
        if result[1]:
            break

    print('#{0} {1}'.format(n, result[L]))
