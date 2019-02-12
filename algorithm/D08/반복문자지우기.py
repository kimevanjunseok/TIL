import sys
sys.stdin = open("반복문자지우기_input.txt")

T = int(input())

for n in range(1, T+1):
    S = list(input())
    cnt = 1
    while cnt != len(S):
        if S[cnt] == S[cnt-1]:
            del S[cnt-1], S[cnt-1]
            cnt = 0
        cnt += 1
    result = len(S)
    print(f"#{n} {result}")