import sys
sys.stdin = open("Labber1_input.txt")

T = 10

for n in range(1, T+1):
    N = int(input())
    L = []
    for i in range(100):
        no = list(map(int, input().split()))
        L += [no]

    for i in range(100):
        if L[99][i] == 2:
            start = i
            break
    up = 98
    while up != 0:
        if start < 99 and L[up][start + 1] == 1:
            while start != 99:
                start += 1
                if L[up][start] == 0:
                    start += -1
                    break
        elif start > 0 and L[up][start - 1] == 1:
            while start != 0:
                start += -1
                if L[up][start] == 0:
                    start += 1
                    break
        # if start == 99:
        #     if L[up][start-1] == 1:
        #         while True:
        #             start += -1
        #             if L[up][start] == 0:
        #                 start += 1
        #                 break

        # elif start == 0:
        #     if L[up][start+1] == 1:
        #         while True:
        #             start += 1
        #             if L[up][start] == 0:
        #                 start += -1
        #                 break

        # elif L[up][start+1] == 1:
        #     while start != 99:
        #         start += 1
        #         if L[up][start] == 0:
        #             start += -1
        #             break
                
        # elif L[up][start-1] == 1:
        #     while start != 0:
        #         start += -1
        #         if L[up][start] == 0:
        #             start += 1
        #             break      
                     
        up += -1

    print(f"#{n} {start}")
