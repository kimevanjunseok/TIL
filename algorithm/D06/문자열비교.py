import sys
sys.stdin = open("sample_input1.txt")

T = int(input())
for n in range(1, T+1):
    test = input()
    S = input()
    result = 0
    cnt_test, cnt = 0, 0
    while True:
        if test[cnt_test] == S[cnt]:
            cnt += 1
            cnt_test += 1
        else:
            cnt = cnt - cnt_test + 1
            cnt_test = 0

        if cnt_test == len(test):
            result = 1
            break
        elif cnt == len(S):
            result = 0
            break
            
    print(f"#{n} {result}")