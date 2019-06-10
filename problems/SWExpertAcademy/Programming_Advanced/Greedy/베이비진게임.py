import sys
sys.stdin = open("베이비진게임_input.txt")

def judge(L):
    if len(L) >= 3:
        for i in range(10):
            if L.count(i) >= 3:
                return True

        L = sorted(list(set(L)))
        n = len(L)

        if n >= 3:
            for i in range(n-2):
                if L[i] + 1 == L[i+1] and L[i+1] + 1 == L[i+2]:
                    return True

    return False

T = int(input())

for n in range(1, T+1):
    arr = list(map(int, input().split()))
    play1 = []
    play2 = []
    result = 0
    for i in range(12):
        if i % 2:
            play2.append(arr[i])
            if judge(play2):
                result = 2
                break

        else:
            play1.append(arr[i])
            if judge(play1):
                result = 1
                break


    print("#{0} {1}".format(n, result))