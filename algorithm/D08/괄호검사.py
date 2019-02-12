import sys
sys.stdin = open("괄호검사_input.txt")

T = int(input())

for n in range(1, T+1):
    S = input()
    cnt = 0
    for i in S:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt += -1
        elif i == "{":
            cnt += 10
        elif i == "}":
            cnt += -10

    if cnt == 0:
        result = 1
    else:
        result = 0

    print(f"#{n} {result}")