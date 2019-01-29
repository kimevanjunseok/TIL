import sys
sys.stdin = open("글자수_input.txt")

T = int(input())

for i in range(1, T+1):
    result = 0
    N = list(input())
    M = input()
    for j in N:
        cnt = 0
        for k in M:
            if j == k:
                cnt += 1
        if result < cnt:
            result = cnt

    print(f"#{i} {result}")