# My solution

def solution(s):
    answer = ''
    if len(s) % 2 != 0:
        answer = s[len(s)//2]
    else:
        answer = s[len(s)//2 -1] + s[len(s)//2]
    return answer

###################################################3

# Other

def solution(s):
    if len(s) % 2:
        return s[len(s) // 2]
    else:
        return s[len(s)//2 - 1 : len(s)//2 + 1]