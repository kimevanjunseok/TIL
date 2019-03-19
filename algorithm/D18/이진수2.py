import sys
sys.stdin = open("이진수2_input.txt")

T = int(input())

for n in range(1, T+1):
    N = float(input())
    cnt = -1
    S = ""
    while True:
        if 2**cnt <= N:
            S += "1"
            N = N - 2**cnt
        else:
            S += "0"

        if N == 0:
            break
        if cnt < -13:
            S = "overflow"
            break

        cnt += -1
    print("#{0} {1}".format(n, S))