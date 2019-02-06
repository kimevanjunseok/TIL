# My solution

def solution(s):
    answer = ''
    cnt = 1
    for i in s:
        cnt += 1
        if i == ' ':
            cnt = 1

        if cnt % 2 == 0:
            answer += i.upper()
        else:
            answer += i.lower()
        
    return answer