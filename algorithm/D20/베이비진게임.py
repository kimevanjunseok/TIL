import sys
sys.stdin = open("베이비진게임_input.txt")

def judge(L):
    List = [[0,1,2], [1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7], [6,7,8], [7,8,9]]
    for i in List:
        if i[0] in L and i[1] in L and i[2] in L:
            return 1

    for i in L:
        if L.count(i) >= 3:
            return 1

T = int(input())

for n in range(1, T+1):
    arr = list(map(int, input().split()))
    play1 = []
    play2 = []
    result = 0
    for i in range(len(arr)):
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

