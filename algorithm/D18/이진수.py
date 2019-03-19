import sys
sys.stdin = open("이진수_input.txt")

T = int(input())

for n in range(1, T+1):
    N, arr = map(str, input().split())

    S = ""
    for i in arr:
        if i in "0123456789":
            i = int(i)
        else:
            i = 10 + (ord(i) - ord("A"))

        for j in range(3, -1, -1):
            if (1<<j)&i:
                S += '1'
            else:
                S += '0'

    print("#{0} {1}".format(n, S))