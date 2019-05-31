import sys
sys.stdin = open("이진수_input.txt")

def binmaker(N):
    D = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    if N in ['A', 'B', 'C', 'D', 'E', 'F']:
        N = D[N]
    else:
        N = int(N)

    S = ['0', '0', '0', '0']
    for i in range(3, -1, -1):
        S[i] = str(N%2)
        N = N // 2
    return "".join(S)
T = int(input())

for n in range(1, T+1):
    N, HEX = map(str, input().split())
    N = int(N)
    result = ""
    for i in HEX:
        result = result + binmaker(i)
    print("#{0} {1}".format(n, result))