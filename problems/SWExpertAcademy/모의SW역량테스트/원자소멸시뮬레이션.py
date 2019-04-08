import sys
sys.stdin = open('원자소멸시뮬레이션_input.txt')

T = int(input())

for n in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    result = 0
    while arr:
        explode = []
        trash = []
        for i in range(len(arr)):
            if arr[i][2] == 0:
                if arr[i][1] == 1000:
                    trash.append(arr[i])
                else:
                    arr[i][1] += 0.5

            elif arr[i][2] == 1:
                if -1000 == arr[i][1]:
                    trash.append(arr[i])
                else:
                    arr[i][1] += -0.5

            elif arr[i][2] == 2:
                if -1000 == arr[i][0]:
                    trash.append(arr[i])
                else:
                    arr[i][0] += -0.5

            elif arr[i][2] == 3:
                if arr[i][0] == 1000:
                    trash.append(arr[i])
                else:
                    arr[i][0] += 0.5

        for i in range(len(trash)):
            arr.remove(trash[i])

        arr.sort()

        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i][0] == arr[j][0]:
                    if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1]:
                        if arr[i] not in explode:
                            explode.append(arr[i])
                        if arr[j] not in explode:
                            explode.append(arr[j])
                else:
                    break

        for i in range(len(explode)):
            arr.remove(explode[i])
            result += explode[i][3]

    print("#{0} {1}".format(n, result))