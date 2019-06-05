import sys
sys.stdin = open("이진수2_input.txt")

T = int(input())

for n in range(1, T+1):
    N = float(input())
    result = ""
    cnt = -1
    com = 1 * 2 ** -1
    while cnt != -14:
        if N > com:
            result = result + "1"

        elif N == com:
            result = result + "1"
            break

        else:
            result = result + "0"
            com += -1 * 2 ** cnt

        cnt += -1
        com += 1 * 2 ** cnt



    print('#{0}'.format(n), end=" ")
    print(result) if len(result) < 13 else print("overflow")