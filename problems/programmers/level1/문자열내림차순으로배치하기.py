# My solution

def solution(s):
    L = []
    for i in s:
        L.append(ord(i))
    L.sort()
    L.reverse()
    answer = ''
    for i in L:
        answer += chr(i)
    return answer