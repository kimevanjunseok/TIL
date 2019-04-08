# My solution

def solution(num):
    cnt = 0
    while True:
        if cnt == 500:
            return -1
        elif num == 1:
            return cnt
        elif num % 2 == 0:
            num = num // 2
            cnt += 1
        elif num % 2 != 0:
            num = num*3 + 1
            cnt += 1