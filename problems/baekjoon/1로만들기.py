N = int(input())

def gogo(x):

    global cnt, min_num

    cnt += 1

    if cnt >= min_num:
        cnt += -1
        return

    if x == 1:
        if min_num > cnt:
            min_num = cnt
        cnt += -1
        return

    if x % 3 == 0:
        gogo(x // 3)

    if x % 2 == 0:
        gogo(x // 2)

    gogo(x - 1)

    cnt += -1

min_num = 99999999999999999999999999
cnt = 0
gogo(N)
print(min_num)








